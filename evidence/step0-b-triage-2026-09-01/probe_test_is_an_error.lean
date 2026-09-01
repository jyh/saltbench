import Imports.AllImports
def f (n : Nat) : Nat := n + 1
#test f 1 = 2     -- should pass
#test f 1 = 99    -- should FAIL
