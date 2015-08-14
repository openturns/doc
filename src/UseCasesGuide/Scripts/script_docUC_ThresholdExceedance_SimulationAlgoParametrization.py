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
myEvent = Event(ouputVector, Greater(), threshold)

# BEGIN_TEX
# Create a Monte Carlo algorithm
myAlgo = MonteCarlo(myEvent)

# The simulation sampling is subsampled in samples of
# BlockSize size (distribution service)
# for MonteCarlo, LHS and Importance Sampling methods, we recommend
# to use BlockSize = number of available CPU if the limit state function is low CPU,
# else it is recommanded to fix BlockSize to a high value (Care : the less OuterSampling
# iterations, the less points in the convergence graph!).
myAlgo.setBlockSize(1)

# Define the 3 stopping criteria :
# Criteria 1 : Define the Maximum Coefficient of variation of the
# probability estimator
myAlgo.setMaximumCoefficientOfVariation(0.1)

# Criteria 2 : Define the Maximum Outer Sampling of the simumlation
myAlgo.setMaximumOuterSampling(10000)

# Criteria 3 :  Define the Maximum  Standard Deviation of the simumlation
myAlgo.setMaximumStandardDeviation(0.1)

# Define the HistoryStrategy to store the values of $P_n$ and $\sigma_n$
# used ot draw the convergence graph

# Null strategy
myAlgo.setConvergenceStrategy(Null())

# Full strategy
myAlgo.setConvergenceStrategy(Full())

# Compact strategy : N points
N = 1000
myAlgo.setConvergenceStrategy(Compact(N))

# Last strategy : N points
myAlgo.setConvergenceStrategy(Last(N))
# END_TEX
