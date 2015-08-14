#!/usr/bin/env python

# BEGIN_TEX
# get input
import sys
inFile = sys.argv[1]
exec(compile(open(inFile).read(), inFile, 'exec'))

# compute
Z = F * E

# write output
h = open('output.py', 'w')
h.write('Z=' + str(Z))
h.close
# END_TEX
