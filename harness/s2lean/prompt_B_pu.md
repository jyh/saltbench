Also deliver an explanation for the next person who builds on this proof. (a) Write the file __EP__/repo/EXPLAIN.md.
Begin it by restating the theorem you proved, `spec_isomorphism`, from its Lean text: name the declaration, quote
its statement, and say in words what it asserts, every quantifier and hypothesis included. Then say in a few
sentences why it holds. Write each sentence from the Lean statement it describes, never from a name, a comment or a
goal. (b) Split the proof into named lemmas inside the `iso_helper_lemmas` section, each with a one-line docstring
(`/-- ... -/`) saying what the lemma states. The proof must still compile without `sorry`.
