from __future__ import print_function
from openturns import *

# Create a function
# for example : myFunction : R^2 --> R^2
#                            (x1, x2) --> (x1 + x2, 'x1*x2)
myFunction = NumericalMathFunction(
    ['x1', 'x2'], ['y1', 'y2'], ['x1 + x2', 'x1*x2'])

# Create an input random vector from a distribution
# for example : a Normal distribution of dimension 2
dist2d = Normal(2)
inputRV = RandomVector(dist2d)

# BEGIN_TEX
# Create the output variable of interest 'output = myFunction(input)'
outputRV = RandomVector(myFunction, inputRV)

# END_TEX
