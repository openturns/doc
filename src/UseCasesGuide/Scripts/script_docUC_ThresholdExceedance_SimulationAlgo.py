from __future__ import print_function
from openturns import *

# Create the model Y = x1 + 2*x2
model = NumericalMathFunction(["x1", "x2"], ["y"], ["x1+2*x2"])

# Create the input distribution and random vector X
inputDist = ComposedDistribution([Normal(), Normal()], IndependentCopula(2))
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
ouputVector = RandomVector(model, inputVector)

# Create the event Y > 4
threshold = 4
# BEGIN_TEX
myEvent = Event(ouputVector, Greater(), threshold)

# Create a Monte Carlo algorithm
myMCAlgo = MonteCarlo(myEvent)

# Create a LHS algorithmscript_docUC_ThresholdExceedance_SimulationAlgo.py
# Care : the copula of the multi-variate distribution must be independent
myLHSAlgo = LHS(myEvent)

# Create a Randomized LHS algorithm
# Care : the copula of the multi-variate distribution must be independent
myRandomizedLHSAlgo = RandomizedLHS(myEvent)

# Create a Importance Sampling  algorithm
# from the distribution myImportanceDistribution
myImportanceDist = Normal(NumericalPoint([4, 0]), IdentityMatrix(2))
myISAlgo = ImportanceSampling(myEvent, myImportanceDist)

# Create a Quasi Monte Carlo algorithm
# Care : the copula of the multi-variate distribution must be independent
myQMCAlgo = QuasiMonteCarlo(myEvent)

# Create a Randomized Quasi Monte Carlo algorithm
# Care : the copula of the multi-variate distribution must be independent
myRandomizedQMCAlgo = RandomizedQuasiMonteCarlo(myEvent)
# END_TEX
