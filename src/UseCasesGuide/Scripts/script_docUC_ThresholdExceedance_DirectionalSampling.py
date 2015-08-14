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
# CASE 1 : Directional Sampling from an event
# Root Strategy by default : Safe And Slow
# Non Linear Solver : Brent algorithm
# Sampling Strategy : Random Direction

# Create a Directional Sampling algorithm
myAlgo = DirectionalSampling(myEvent)

# CASE 2 : Directional Sampling from an event, a root strategy
# and a directional sampling strategy
# Root Strategy by default : MediumSafe
# Non Linear Solver : Brent algorithm
# Sampling Strategy : Orthogonal Direction

# Create a Directional Sampling algorithm
# dimension of the input random vector
dimInput = 2
myAlgo2 = DirectionalSampling(myEvent, RootStrategy(
    MediumSafe()), SamplingStrategy(OrthogonalDirection(dimInput, 2)))

# END_TEX
