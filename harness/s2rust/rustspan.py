#!/usr/bin/env python3
"""rustspan.py — the ONLY place that reads Rust source structurally. A deliberately small,
deliberately LOUD lexer: it tracks line comments, block comments, char and string literals
(including raw strings) and brace depth, and it REFUSES rather than guesses.

Everything downstream (the view builder, the assembler's split, the helpers placement) is
defined in terms of byte offsets this module returns, and every split it produces is checked
by a byte-exact reconstruction in build_views_verus.py. A mis-located span therefore cannot
pass silently: it fails the reconstruction and the task is refused, never drawn.

importable only; no CLI.
"""

class SpanError(Exception):
    """Raised when the source cannot be lexed unambiguously. Always a REFUSE, never a guess."""


def scan(src):
    """Yield (i, depth, in_code) for every byte offset i.

    depth is the brace nesting depth BEFORE the byte at i is consumed. in_code is False inside
    a comment or a literal. Implemented as a generator so callers can stop early on big files.
    """
    n = len(src)
    i = 0
    depth = 0
    while i < n:
        c = src[i]
        # line comment
        if c == "/" and i + 1 < n and src[i + 1] == "/":
            j = src.find("\n", i)
            j = n if j < 0 else j
            while i < j:
                yield i, depth, False
                i += 1
            continue
        # block comment (Rust nests them)
        if c == "/" and i + 1 < n and src[i + 1] == "*":
            level = 0
            j = i
            while j < n:
                if src[j] == "/" and j + 1 < n and src[j + 1] == "*":
                    level += 1; j += 2; continue
                if src[j] == "*" and j + 1 < n and src[j + 1] == "/":
                    level -= 1; j += 2
                    if level == 0:
                        break
                    continue
                j += 1
            if level != 0:
                raise SpanError("unterminated block comment at offset %d" % i)
            while i < j:
                yield i, depth, False
                i += 1
            continue
        # raw string  r"..."  r#"..."#  (br"..." too)
        if c in "rb" and _raw_start(src, i):
            k = i
            while src[k] not in "r":
                k += 1
            k += 1
            hashes = 0
            while k < n and src[k] == "#":
                hashes += 1; k += 1
            if k >= n or src[k] != '"':
                raise SpanError("malformed raw string at offset %d" % i)
            close = '"' + "#" * hashes
            j = src.find(close, k + 1)
            if j < 0:
                raise SpanError("unterminated raw string at offset %d" % i)
            j += len(close)
            while i < j:
                yield i, depth, False
                i += 1
            continue
        # ordinary string
        if c == '"':
            j = i + 1
            while j < n:
                if src[j] == "\\":
                    j += 2; continue
                if src[j] == '"':
                    j += 1; break
                j += 1
            else:
                raise SpanError("unterminated string at offset %d" % i)
            while i < j:
                yield i, depth, False
                i += 1
            continue
        # char literal or lifetime: only treat as a literal when it closes on the same line
        if c == "'":
            j = _char_end(src, i)
            if j is not None:
                while i < j:
                    yield i, depth, False
                    i += 1
                continue
        yield i, depth, True
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0:
                raise SpanError("unbalanced '}' at offset %d" % i)
        i += 1


def _raw_start(src, i):
    if src[i] == "b":
        if i + 1 >= len(src) or src[i + 1] != "r":
            return False
        i += 1
    j = i + 1
    while j < len(src) and src[j] == "#":
        j += 1
    return j < len(src) and src[j] == '"'


def _char_end(src, i):
    """End offset of a char literal starting at i, or None if this is a lifetime."""
    n = len(src)
    j = i + 1
    if j < n and src[j] == "\\":
        j += 2
    elif j < n:
        j += 1
    if j < n and src[j] == "'":
        return j + 1
    return None


def code_map(src):
    """(depths, incode) as lists indexed by byte offset. depth is the depth BEFORE the byte."""
    depths = [0] * len(src)
    incode = [False] * len(src)
    for i, d, c in scan(src):
        depths[i] = d
        incode[i] = c
    return depths, incode


def match_brace(src, open_idx, incode):
    """Offset of the '}' matching the '{' at open_idx. Raises if unmatched."""
    if src[open_idx] != "{" or not incode[open_idx]:
        raise SpanError("offset %d is not a code '{'" % open_idx)
    depth = 0
    for j in range(open_idx, len(src)):
        if not incode[j]:
            continue
        if src[j] == "{":
            depth += 1
        elif src[j] == "}":
            depth -= 1
            if depth == 0:
                return j
    raise SpanError("unmatched '{' at offset %d" % open_idx)
