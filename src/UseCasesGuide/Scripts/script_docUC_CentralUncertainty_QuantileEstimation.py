from __future__ import print_function
from openturns import *
from math import sqrt

# Create the model Y = x1^2 + x2
model = NumericalMathFunction(["x1", "x2"], ["y"], ["x1^2+x2"])

# Create the input distribution and random vector X
myCorMat = CorrelationMatrix(2)
myCorMat[0, 1] = -0.6
inputDist = Normal([0., 0.], myCorMat)
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
output = RandomVector(model, inputVector)

# BEGIN_TEX
# Order of the quantile to estimate
alpha = 0.95

# Confidence level of the estimation
beta = 0.90

# Empirical Quantile Estimator

# Get the numerical sample of the variable
N = 10 ** 4
outputNumericalSample = output.getSample(N)

# Get the empirical estimation
empiricalQuantile = outputNumericalSample.computeQuantile(alpha)

# Confidence interval of the Empirical Quantile Estimator
# Get the indices of the confidence interval bounds
aAlpha = Normal(1).computeQuantile((1 + beta) / 2)[0]
min = int(N * alpha - aAlpha * sqrt(N * alpha * (1 - alpha)))
max = int(N * alpha + aAlpha * sqrt(N * alpha * (1 - alpha)))

# Get the sorted numerical sample
sortedOutputNumericalSample = outputNumericalSample.sort()

# Get the Confidence interval [infQuantile, supQuantile]
infQuantile = sortedOutputNumericalSample[min - 1]
supQuantile = sortedOutputNumericalSample[max - 1]


# Wilks Quantile Estimator

# Get the Wilks number : the minimal number of realizations to perform
# in order to garantee that the empirical quantile alpha be greater than
# the theoretical one with a probability of beta,
# when the empirical quantile is evaluated with the (n-i)th maximum of the sample.
# For the example, we consider alpha=0.95, beta=0.90 and i=3
# By default, i=0 (empirical quantile = maximum of the sample)
i = 3
wilksNumber = Wilks.ComputeSampleSize(0.95, 0.90, i)

# Get the numerical sample of the variable
outputNumericalSample = output.getSample(wilksNumber)

# Get the sorted numerical sample
sortedOutputNumericalSample = outputNumericalSample.sort()

# Calculate the indice of the Wilks quantile
indice = wilksNumber - i

# Get the empirical estimation
wilksQuantile = sortedOutputNumericalSample[indice]
print("wilks Quantile 0.95 = ", wilksQuantile)
# END_TEX
