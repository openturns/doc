from __future__ import print_function
from openturns import *

# BEGIN_TEX
# Create the function g : R^d --> R^q
# for example : R^2 --> R^2
#               (x1,x2) --> (x1^2, x1+x2)
g = NumericalMathFunction(['x1', 'x2'],  ['x1^2', 'x1+x2'])

# Create the function h : R^n*R^d --> R^q
# for example : R^2*R^2 --> R
#               (t1,t2,x1,x2) --> (t1+t2+x1^2+x2^2)
h = NumericalMathFunction(['t1', 't2', 'x1', 'x2'],  ['t1+t2+x1^2+x2^2'])

###########################################
# Creation of a spatial dynamical function
###########################################

# Convert g : R^d --> R^q into a spatial fucntion
# n is the dimension of the mesh
# of the field on wich g will be applied
n = 2
mySpatialFunction = SpatialFunction(g, n)
print("spatial function=", mySpatialFunction)

###########################################
# Creation of a temporal dynamical function
###########################################

# Convert h: R^n*R^d --> R^q into a temporal function
# n is the dimension of the mesh
# here n = dimension (t1,t2)
n = 2
myTemporalFunction = TemporalFunction(h, n)
print("temporal function=", myTemporalFunction)

# END_TEX
