#!/usr/bin/env python

# BEGIN_TEX
from __future__ import print_function
import openturns as ot

def compute_point( X ):
    E=X[0]
    F=X[1]
    Y = [E * F]
    return Y

model = ot.PythonFunction(2, 1, compute_point)
out_sample = model( ot.NumericalSample([[2, 3], [5, 8]]) )
print(out_sample)
#...
# END_TEX
