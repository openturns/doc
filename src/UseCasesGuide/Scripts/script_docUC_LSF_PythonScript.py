from __future__ import print_function
from openturns import *

# BEGIN_TEX
################################
# CASE 1 : function : R^4 --> R
################################

# Create here the python lines to define the implementation of the function

# In order to be able to use that function with the openturns library,
# it is necessary to define a class which derives from OpenTURNSPythonFunction


class modelePYTHON(OpenTURNSPythonFunction):
    # that following method defines the input size (4) and the output size (1)

    def __init__(self):
        OpenTURNSPythonFunction.__init__(self, 4, 1)

    # that following method gives the implementation of modelePYTHON
    def _exec(self, x):
        E = x[0]
        F = x[1]
        L = x[2]
        I = x[3]
        return [-(F * L * L * L) / (3. * E * I)]

# Use that function defined in the script python
# with the openturns library
# Create a NumericalMathFunction from modelePYTHON
model1 = NumericalMathFunction(modelePYTHON())


################################
# CASE 2 : function : R^3 --> R^2
################################

# Create here the python lines to define the implementation of the function

# In order to be able to use that function with the openturns library,
# we can use the constructor PythonFunction from a regular python function.

def f(x):
    a = x[0]
    b = x[1]
    c = x[2]
    y = [-a * a, a * b * c]
    return y

model2 = PythonFunction(3, 2, f)

# END_TEX

print((model2([1.] * 3)))
