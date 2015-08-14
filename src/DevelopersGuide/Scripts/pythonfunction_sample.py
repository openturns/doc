#!/usr/bin/env python

# BEGIN_TEX
from __future__ import print_function
import openturns as ot
import numpy as np

def exec_sample( Xs ):
    # speedup using numpy
    import numpy as np
    XsT = np.array(Xs).T
    return np.atleast_2d(np.multiply(XsT[0], XsT[1])).T
    #return [[x[0] * x[1]] for x in Xs]

model = ot.PythonFunction(2, 1, func_sample=exec_sample)
#...
# END_TEX
