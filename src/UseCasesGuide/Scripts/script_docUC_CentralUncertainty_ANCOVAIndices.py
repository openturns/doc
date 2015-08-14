from __future__ import print_function
from openturns import *

# Create the model (x1,x2) --> (y) = (4.*x1+5.*x2)
model = NumericalMathFunction(["x1", "x2"], ["y"], ["4.*x1+5.*x2"])

# Create the input independant joint distribution
inputDist = ComposedDistribution(
    DistributionCollection([Normal(), Normal()]), IndependentCopula(2))
inputDist.setDescription(['X1', 'X2'])

# Create the correlated input distribution
S = CorrelationMatrix(2)
S[1, 0] = 0.3
R = NormalCopula().GetCorrelationFromSpearmanCorrelation(S)
myCopula = NormalCopula(R)
myCorrelatedInputDist = ComposedDistribution([Normal(), Normal()], myCopula)

# Create the input sample taking account the correlation
size = 2000
sample = myCorrelatedInputDist.getSample(size)

# Create an orthogonal basis
enumerateFunction = EnumerateFunction(2)
productBasis = OrthogonalProductPolynomialFactory(
    [HermiteFactory(), HermiteFactory()], enumerateFunction)
# Set an adaptive strategy
adaptiveStrategy = FixedStrategy(
    productBasis, enumerateFunction.getStrataCumulatedCardinal(4))
# Set a projection strategy
samplingSize = 250
projectionStrategy = LeastSquaresStrategy(MonteCarloExperiment(samplingSize))

# Create the polynomial chaos expansion
algo = FunctionalChaosAlgorithm(
    model, inputDist, adaptiveStrategy, projectionStrategy)
algo.run()
result = FunctionalChaosResult(algo.getResult())

# BEGIN_TEX
# Initialize computation of the indices
ancova = ANCOVA(result, sample)
# Compute the ANCOVA indices (first order and uncorrelated indices are
# computed together)
indices = ancova.getIndices()
# Retrieve uncorrelated indices
uncorrelatedIndices = ancova.getUncorrelatedIndices()
# Retrieve correlated indices
correlatedIndices = indices - uncorrelatedIndices

# Print indices
print("ANCOVA indices ", indices)
print("ANCOVA uncorrelated indices ", uncorrelatedIndices)
print("ANCOVA correlated indices ", correlatedIndices)

    # END_TEX
