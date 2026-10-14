# Generic protobuf walk over agy conversations/<id>.db gen_metadata blobs: sum every varint by its FIELD PATH, so the usage field can be
# identified against a KNOWN total (the parent conversation's agy-meter per_key) before it is trusted on a sub-agent's db.
import sqlite3, sys, collections
def varint(b, i):
    r = s = 0
    while True:
        c = b[i]; i += 1; r |= (c & 0x7f) << s; s += 7
        if not c & 0x80: return r, i
def walk(b, path, out, depth=0):
    i = 0
    try:
        while i < len(b):
            key, i = varint(b, i); f, t = key >> 3, key & 7
            if f == 0: return False
            if t == 0: v, i = varint(b, i); out[path + (f,)] += v
            elif t == 1: i += 8
            elif t == 5: i += 4
            elif t == 2:
                n, i = varint(b, i); sub = b[i:i+n]; i += n
                if depth < 6: walk(sub, path + (f,), out, depth + 1)
            else: return False
        return i == len(b)
    except IndexError: return False
if __name__ == '__main__':
  for db in sys.argv[1:]:
      out = collections.Counter()
      for (d,) in sqlite3.connect("file:%s?mode=ro&immutable=1" % db, uri=True).execute("select data from gen_metadata"):
          walk(d, (), out)
      print("==", db.split('/')[-1][:8], len(out), "paths")
      for p, v in sorted(out.items(), key=lambda x: -x[1])[:40]:
          if 1000 < v < 10**8: print("  ", ".".join(map(str, p)), v)
