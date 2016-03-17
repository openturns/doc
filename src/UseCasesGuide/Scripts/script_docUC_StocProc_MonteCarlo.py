from __future__ import print_function
from openturns import *


# Create a time grid
tMin = 0.0
timeStep = 0.1
n = 100
myTimeGrid = RegularGrid(tMin, timeStep, n)

# Create a normal process
amplitude = NumericalPoint([5.0])
scale = NumericalPoint([3.0])
model = ExponentialCauchy(amplitude, scale)
myProcess = TemporalNormalProcess(model, myTimeGrid)

# Create the domain A
# for example in dimension 1 : [2.,5.]
# Lower bound vector
lowerBound = NumericalPoint([2.0])
# Upper bound vector
upperBound = NumericalPoint([5.0])
myDomainA = Interval(lowerBound, upperBound)

# BEGIN_TEX
# Create an event from a Process and a Domain
# myEvent = EventProcess(myProcess, myDomain)
myEvent = Event(myProcess, myDomainA)

# Create a Monte-Carlo algorithm based on myEvent
myMonteCarloAlgo = MonteCarlo(myEvent)

# Define the maximum number of simulations
myMonteCarloAlgo.setMaximumOuterSampling(1000)

# Define the block size
myMonteCarloAlgo.setBlockSize(100)

# Define the maximum coefficient of variation
myMonteCarloAlgo.setMaximumCoefficientOfVariation(0.0025)

# Run the algorithm
myMonteCarloAlgo.run()

# Get the result
result = myMonteCarloAlgo.getResult()
print(result)

# Draw the convergence graph
convGraph = myMonteCarloAlgo.drawProbabilityConvergence(0.95)
# END_TEX
