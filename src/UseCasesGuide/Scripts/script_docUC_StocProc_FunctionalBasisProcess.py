from __future__ import print_function
from openturns import *

# Create the distribution of the random coefficients
# For example in dimension K=2 : two coefficients
coefDist = ComposedDistribution(
    [Exponential(0.2), Normal()], ClaytonCopula(0.2))

# Create a basis function
# for example phi : R --> R^3
phi_1 = NumericalMathFunction(["t"], ["1", "t", "t^2"])
phi_2 = NumericalMathFunction(["t"], ["t", "t^2", "t^3"])
myBasis = NumericalMathFunctionCollection([phi_1, phi_2])

# Create the RegularGrid
tMin = 0.0
timeStep = 0.1
n = 100
myMesh = RegularGrid(tMin, timeStep, n)

# BEGIN_TEX
# Create the output process of interest
myOutputProcess = FunctionalBasisProcess(coefDist, Basis(myBasis), myMesh)
# END_TEX
