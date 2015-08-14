from __future__ import print_function
from openturns import *

# Create a collection of scalar function R ^n --> R
# for example 2 functions R^2 --> R
f1 = NumericalMathFunction(['x1', 'x2'], ['y'], ['x1+x2'])
f2 = NumericalMathFunction(['x1', 'x2'], ['y'], ['x1*x2'])
scalFctColl = NumericalMathFunctionCollection([f1, f2])

# Create a collection of vectorial function R ^n --> R^p
# for example 2 functions R^2 --> R^2
f3 = NumericalMathFunction(['x1', 'x2'], ['y1', 'y2'], ['2*x1+x2', 'x1+2*x2'])
f4 = NumericalMathFunction(['x1', 'x2'], ['y1', 'y2'], ['x1*x2', 'x1-x2'])
vectFctColl = NumericalMathFunctionCollection([f3, f4])

# Create a list of scalar weights
# for example 2 coefficients
scalWeight = NumericalPoint([1.2, 2.3])

# Create a list of vectorial weights
# for example 2 coefficientsof dimension 3
vectWeight = NumericalSample(2, 3)
vectWeight[0] = NumericalPoint([1., 2., 3.])
vectWeight[1] = NumericalPoint([4., 5., 6.])

# Create a scalar function
function = f1

# BEGIN_TEX
# Create the scalar linear combination of vectorial functions
linComb = NumericalMathFunction(vectFctColl, scalWeight)

# Create the vectorial linear combination of scalar functions
vectLinComb = NumericalMathFunction(scalFctColl, vectWeight)

# Create the agregated function
agregFct = NumericalMathFunction(vectFctColl)

# Create the indicator function
# define a threshold and a comparison operator
threshold = 3.0
comparisonOperator = Greater()
agregFunction = NumericalMathFunction(function, comparisonOperator, threshold)
# END_TEX
