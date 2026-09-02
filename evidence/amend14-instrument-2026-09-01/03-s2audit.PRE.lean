/-
s2audit.lean — the harness-owned KERNEL AUDIT of one compiled canonical module (repair round 1, D4 step 4).
Runs OUTSIDE the agent's elaboration: it never imports or elaborates the canonical file, it only reads its
olean (Lean.readModuleData: no `initialize` runs, no command elaborators fire) and

  1. REPLAYS every constant of the module through the kernel into a fresh environment that holds only
     `Imports.AllImports` (Lean.Environment.replay, the lean4checker core). A kernel rejection — including the
     debug.skipKernelTC bypass of refuter F4 — is reported as replay_ok=false with the kernel's message.
  2. Compares, as Expr (alpha-equivalence, `==`), the TYPE (and kind, and level params) of every frozen
     declaration of the stage against the PRISTINE olean (frozen statements, sorry bodies, no agent text), and
     for problem_spec ALSO the VALUE. A notation/macro/instance that changes the elaborated meaning of a frozen
     statement (refuter F3) shows up here as a differing Expr.
  3. Collects the axioms of the stage's audited declarations over the REPLAYED environment
     (Lean.CollectAxioms — a pure function over the environment; no `#print axioms` line exists any more, so
     refuter F6's elab_rules hijack has nothing to hijack). Allowlist: propext, Classical.choice, Quot.sound.
  4. Optionally compares generated_spec's VALUE with the stage-A canonical olean (a_body_value_identical).

usage (in LEANPROJ, with lake's environment):
  lean --run s2audit.lean <canonical.olean> <pristine.olean> <A|B|C> [<a_canonical.olean>|-]
stdout: one JSON object
  {replay_ok, replay_error, statements:{name:{type_identical, value_identical|null}}, statements_identical,
   statement_diffs:[names], axioms:{name:[…]}, axioms_ok, a_body_value_identical:bool|null,
   n_constants, constants:[names], error?}
exit 0 when the audit ran (whatever its verdict); 2 on a harness error (bad args, unreadable olean).
-/
import Lean
open Lean

namespace S2Audit

def allow : List Name := [``propext, ``Classical.choice, ``Quot.sound]

/-- Frozen declarations per stage: (name, compare the value too?). -/
def frozen (stage : String) : List (Name × Bool) :=
  match stage with
  | "A" => [(`generated_spec, false)]
  | "B" => [(`generated_spec, false), (`problem_spec, true), (`spec_isomorphism, false)]
  | "C" => [(`problem_spec, true), (`implementation, false), (`correctness, false)]
  | _   => []

def kind : ConstantInfo → String
  | .defnInfo _   => "defn"   | .thmInfo _    => "thm"    | .axiomInfo _ => "axiom"
  | .opaqueInfo _ => "opaque" | .quotInfo _   => "quot"   | .inductInfo _ => "induct"
  | .ctorInfo _   => "ctor"   | .recInfo _    => "rec"

def value? : ConstantInfo → Option Expr
  | .defnInfo v => some v.value | .thmInfo v => some v.value | .opaqueInfo v => some v.value | _ => none

def toMap (md : ModuleData) : Std.HashMap Name ConstantInfo := Id.run do
  let mut m : Std.HashMap Name ConstantInfo := {}
  for ci in md.constants do
    m := m.insert ci.name ci
  return m

/-- Axiom collection over a lookup (the module's own constants, then the import environment): the same
ConstantInfos the replay checks, so the axioms are reported even when the kernel rejects the module. -/
partial def collectAx (lookup : Name → Option ConstantInfo) (c : Name) : StateM (NameSet × Array Name) Unit := do
  let collectExpr (e : Expr) : StateM (NameSet × Array Name) Unit := e.getUsedConstants.forM (collectAx lookup)
  let (visited, _) ← get
  unless visited.contains c do
    modify fun (v, a) => (v.insert c, a)
    match lookup c with
    | some (.axiomInfo v)  => modify fun (vs, a) => (vs, a.push c); collectExpr v.type
    | some (.defnInfo v)   => collectExpr v.type; collectExpr v.value
    | some (.thmInfo v)    => collectExpr v.type; collectExpr v.value
    | some (.opaqueInfo v) => collectExpr v.type; collectExpr v.value
    | some (.quotInfo _)   => pure ()
    | some (.ctorInfo v)   => collectExpr v.type
    | some (.recInfo v)    => collectExpr v.type
    | some (.inductInfo v) => collectExpr v.type; v.ctors.forM (collectAx lookup)
    | none                 => pure ()

def axiomsOf (lookup : Name → Option ConstantInfo) (n : Name) : Array Name :=
  let (_, (_, a)) := (collectAx lookup n).run ({}, #[])
  a.qsort Name.lt

def names (a : Array Name) : Json := Json.arr (a.map fun n => Json.str n.toString)

def run (canon pristine stage : String) (aOlean? : Option String) : IO Json := do
  initSearchPath (← findSysroot)
  let env0 ← importModules (loadExts := false) #[{ module := `Imports.AllImports }] {} (trustLevel := 1024)
  let (mdC, _regionC) ← readModuleData canon
  let (mdP, _regionP) ← readModuleData pristine
  let mapC := toMap mdC
  let mapP := toMap mdP
  -- 1. kernel replay
  let (replayOk, replayErr, envC?) ← try
      let envC ← env0.replay mapC
      pure (true, "", some envC)
    catch e => pure (false, toString e, none)
  -- 2. statements vs pristine
  let mut stmts : Array (String × Json) := #[]
  let mut diffs : Array Name := #[]
  for (n, cmpVal) in frozen stage do
    match mapP[n]?, mapC[n]? with
    | some cp, some cc =>
      let tId := cp.type == cc.type && kind cp == kind cc && cp.levelParams == cc.levelParams
      let vId? : Option Bool := if cmpVal then some (value? cp == value? cc) else none
      if !tId || vId? == some false then diffs := diffs.push n
      stmts := stmts.push (n.toString, Json.mkObj [
        ("type_identical", tId), ("value_identical", match vId? with | some b => Json.bool b | none => Json.null),
        ("kind_canonical", kind cc), ("kind_pristine", kind cp)])
    | cp?, cc? =>
      diffs := diffs.push n
      stmts := stmts.push (n.toString, Json.mkObj [
        ("type_identical", false), ("value_identical", if cmpVal then Json.bool false else Json.null),
        ("present_canonical", cc?.isSome), ("present_pristine", cp?.isSome)])
  -- 3. axioms over the module's constants ∪ the import environment (reported whatever the replay said)
  let lookup : Name → Option ConstantInfo := fun n => (mapC[n]?).orElse fun _ => env0.find? n
  let mut axs : Array (String × Json) := #[]
  let mut axOk := true
  for (n, _) in frozen stage do
    let a := axiomsOf lookup n
    axs := axs.push (n.toString, names a)
    if !(a.all fun x => allow.contains x) then axOk := false
    if (mapC[n]?).isNone then axOk := false
  let _ := envC?
  -- 4. stage-A body value
  let aId ← match aOlean? with
    | none => pure Json.null
    | some p =>
      let (mdA, _regionA) ← readModuleData p
      let mapA := toMap mdA
      pure (Json.bool ((mapA[`generated_spec]? >>= value?) == (mapC[`generated_spec]? >>= value?)))
  -- AP-3: names referenced by an audited decl that resolve in NEITHER the module nor the import env — fail closed
  let mut unknown : Array Name := #[]
  for (n, _) in frozen stage do
    if (lookup n).isNone then unknown := unknown.push n
  axOk := axOk && unknown.isEmpty   -- mut reassign (Lean forbids shadowing a let mut)
  return Json.mkObj [
    ("replay_ok", replayOk), ("replay_error", replayErr), ("unknown", names unknown),
    ("statements", Json.mkObj stmts.toList), ("statements_identical", diffs.isEmpty), ("statement_diffs", names diffs),
    ("axioms", Json.mkObj axs.toList), ("axioms_ok", axOk), ("a_body_value_identical", aId),
    ("n_constants", mdC.constants.size), ("constants", names mdC.constNames)]

end S2Audit

def main (args : List String) : IO UInt32 := do
  match args with
  | canon :: pristine :: stage :: rest =>
    let aOlean? := match rest with | a :: _ => if a == "-" then none else some a | [] => none
    try
      let j ← S2Audit.run canon pristine stage aOlean?
      IO.println j.compress
      return 0
    catch e =>
      IO.println (Json.mkObj [("error", toString e)]).compress
      return 2
  | _ =>
    IO.println (Json.mkObj [("error", "usage: s2audit.lean <canonical.olean> <pristine.olean> <A|B|C> [<a_canonical.olean>|-]")]).compress
    return 2
