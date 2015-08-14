from __future__ import print_function
from openturns import *

# BEGIN_TEX
####################
# Case where f : R^n --> R^p
####################

# Describe the input vector of dimension 2
inputFunc = Description(("x1", "x2"))

# Describe the output vector of dimension 1
outputFunc = Description(("Output 1",))

# Give the formulas
formulas = Description(outputFunc.getSize())
formulas[0] = "-(6 - x1 + x2^2)"
print("formulas=", formulas)

# Create the analytical function
myAnalyticalFunction = NumericalMathFunction(inputFunc, outputFunc, formulas)

# or directly
myAnalyticalFunction_2 = NumericalMathFunction(
    ("x1", "x2"), ("Output 1",), ("-(6 - x1 + x2^2)",))

####################
# Case where f : R --> R
####################

# For example : x --> x^2
scalarF = NumericalMathFunction('x', 'x^2')

# END_TEX
