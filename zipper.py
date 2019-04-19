import sys

import zipreader.reader as zr

filepath = sys.argv[1]
gzr = zr.Reader(filepath)
print(gzr.read())