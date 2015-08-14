from __future__ import print_function
from openturns import *

# Create the model (x1,x2) --> (y1,y2) = (x1^2 + x2, x2^2+x1)
model = NumericalMathFunction(
    ["x1", "x2"], ["y1", "y2"], ["x1^2+x2", "x2^2+x1"])

inputDist = ComposedDistribution(
    DistributionCollection([Normal(), Normal()]), IndependentCopula(2))
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
output = RandomVector(model, inputVector)


# BEGIN_TEX
# Create a random sample of the output variabe of interest of size 1000
size = 1000
outputSample = output.getSample(size)

# Get the empirical mean
empiricalMean = outputSample.computeMean()
print("Empirical Mean = ", empiricalMean)

# Get the empirical covariance matrix
empiricalCovarianceMatrix = outputSample.computeCovariance()
print("Empirical Covariance Matrix = ")
print(empiricalCovarianceMatrix)

# Get the Cholesky factor of the covariance matrix C
# C = LL^t
choleskyMatrix = outputSample.computeStandardDeviation()
print("chol = ")
print(choleskyMatrix)
# END_TEX
