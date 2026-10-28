#![allow(unused_imports)]
use vstd::prelude::*;

verus! {
// ===== INTERFACE REGION BEGIN =====
/// One call and the answer it gave.  The tests record what they did in this form; you do not
/// have to use it.
#[derive(Clone, Debug, PartialEq, Eq)]
pub enum Op {
    Crc32 { msg: Vec<u8>, result: u32 },
}

/// THE FUNCTION TO IMPLEMENT: the CRC-32 of a message.  The signature line is fixed; the body
/// is yours, and so is anything else you write below the region.
pub fn crc32(msg: &[u8]) -> (r: u32)
    ensures r == expected_crc32(msg@)
{

    let mut crc: u32 = 0xFFFFFFFF;
    let mut i = 0;
    while i < msg.len()
        invariant
            0 <= i && i <= msg.len(),
            crc == crc32_seq(msg@.subrange(0, i as int))
        decreases msg.len() - i
    {
        let byte = msg[i];
        let idx = ((crc ^ (byte as u32)) & 0xFFu32) as usize;
        proof { assert(((crc ^ (byte as u32)) & 0xFFu32) < 256u32) by (bit_vector); }
        
        proof { lemma_byte_step_equiv(crc, byte); }
        proof { lemma_table(idx as u8); }
        
        crc = (crc >> 8u32) ^ CRC32_TABLE[idx];
        i = i + 1;
        assert(msg@.subrange(0, i as int).drop_last() == msg@.subrange(0, (i - 1) as int));
    }
    assert(msg@.subrange(0, msg.len() as int) == msg@);
    crc ^ 0xFFFFFFFF

}
// ===== INTERFACE REGION END =====

pub open spec fn crc32_bit_step(crc: u32, bit: u32) -> u32 {
    if (crc ^ bit) & 1 == 1 {
        (crc >> 1) ^ 0xEDB88320
    } else {
        crc >> 1
    }
}

pub open spec fn crc32_byte_step(crc: u32, byte: u8) -> u32 {
    let crc1 = crc32_bit_step(crc, (byte as u32));
    let crc2 = crc32_bit_step(crc1, (byte as u32) >> 1);
    let crc3 = crc32_bit_step(crc2, (byte as u32) >> 2);
    let crc4 = crc32_bit_step(crc3, (byte as u32) >> 3);
    let crc5 = crc32_bit_step(crc4, (byte as u32) >> 4);
    let crc6 = crc32_bit_step(crc5, (byte as u32) >> 5);
    let crc7 = crc32_bit_step(crc6, (byte as u32) >> 6);
    let crc8 = crc32_bit_step(crc7, (byte as u32) >> 7);
    crc8
}

pub open spec fn crc32_seq(msg: Seq<u8>) -> u32
    decreases msg.len()
{
    if msg.len() == 0 {
        0xFFFFFFFF
    } else {
        crc32_byte_step(crc32_seq(msg.drop_last()), msg.last())
    }
}

pub open spec fn expected_crc32(msg: Seq<u8>) -> u32 {
    crc32_seq(msg) ^ 0xFFFFFFFF
}

pub open spec fn trace_ok(t: Seq<Op>) -> bool {
    forall |i: int| 0 <= i && i < t.len() ==>
        match #[trigger] t[i] {
            Op::Crc32 { msg, result } => result == expected_crc32(msg@),
        }
}

pub fn check_trace(t: &Vec<Op>) -> (r: bool)
    ensures r == trace_ok(t@)
{
    let mut i = 0;
    let mut r = true;
    while i < t.len()
        invariant
            0 <= i && i <= t.len(),
            r == (forall |j: int| 0 <= j && j < i ==>
                match #[trigger] t@[j] {
                    Op::Crc32 { msg, result } => result == expected_crc32(msg@),
                })
        decreases t.len() - i
    {
        let op = &t[i];
        match op {
            Op::Crc32 { msg, result } => {
                r = r && (*result == compute_expected_crc32(msg));
            }
        }
        i = i + 1;
    }
    r
}

fn exec_crc32_bit_step(crc: u32, bit: u32) -> (r: u32)
    ensures r == crc32_bit_step(crc, bit)
{
    if (crc ^ bit) & 1 == 1 {
        (crc >> 1) ^ 0xEDB88320
    } else {
        crc >> 1
    }
}

fn exec_crc32_byte_step(crc: u32, byte: u8) -> (r: u32)
    ensures r == crc32_byte_step(crc, byte)
{
    let crc1 = exec_crc32_bit_step(crc, byte as u32);
    let crc2 = exec_crc32_bit_step(crc1, (byte as u32) >> 1);
    let crc3 = exec_crc32_bit_step(crc2, (byte as u32) >> 2);
    let crc4 = exec_crc32_bit_step(crc3, (byte as u32) >> 3);
    let crc5 = exec_crc32_bit_step(crc4, (byte as u32) >> 4);
    let crc6 = exec_crc32_bit_step(crc5, (byte as u32) >> 5);
    let crc7 = exec_crc32_bit_step(crc6, (byte as u32) >> 6);
    let crc8 = exec_crc32_bit_step(crc7, (byte as u32) >> 7);
    crc8
}

fn compute_expected_crc32(msg: &Vec<u8>) -> (r: u32)
    ensures r == expected_crc32(msg@)
{
    let mut crc: u32 = 0xFFFFFFFF;
    let mut i = 0;
    while i < msg.len()
        invariant
            0 <= i && i <= msg.len(),
            crc == crc32_seq(msg@.subrange(0, i as int))
        decreases msg.len() - i
    {
        crc = exec_crc32_byte_step(crc, msg[i]);
        i = i + 1;
        assert(msg@.subrange(0, i as int).drop_last() == msg@.subrange(0, (i - 1) as int));
    }
    assert(msg@.subrange(0, msg.len() as int) == msg@);
    crc ^ 0xFFFFFFFF
