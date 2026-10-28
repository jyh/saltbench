use vstd::prelude::*;
/* a block comment
   over two lines */
verus! {
pub struct Pool {
    pub slots: Vec<u64>,
    pub ghost model: Seq<u64>,
}

impl Pool {
    pub closed spec fn view(&self) -> Seq<u64> {
        self.model
    }

    #[verifier::type_invariant]
    spec fn inv(&self) -> bool { self.slots@ == self.model }

    pub fn push(&mut self, v: u64)
        requires
            old(self).slots.len() < 100,
        ensures
            self.view() == old(self).view().push(v),
    {
        let s = "{ an unbalanced brace and paren (";
        self.slots.push(v);
        assert(self.slots@ == old(self).slots@.push(v)) by {
            reveal(Pool::view);
        }
        proof {
            self.model = self.model.push(v);
        }
    }
}

proof fn lemma_len(s: Seq<u64>)
    requires s.len() > 0,
    ensures s.drop_last().len() == s.len() - 1,
{
}

pub fn helper(x: u64) -> u64
    decreases x,
{
    if x == 0 { 0 } else { helper(x - 1) } // trailing comment
}
} // verus!

fn outside(a: u32) -> u32 {
    assert!(a < 100);
    a + 1
}

#[cfg(test)]
mod tests {
    #[test]
    fn t() { assert_eq!(super::outside(1), 2); }
}
