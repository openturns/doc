from __future__ import print_function
from openturns import *

# Create the RegularGrid
tMin = 0.
timeStep = 0.1
n = 100
myTimeGrid = RegularGrid(tMin, timeStep, n)

# Create the distribution of the random walk
# Here dimension 2
myDist = ComposedDistribution([Normal(), Exponential(0.2)], ClaytonCopula(0.5))


# Create the origin point
# here at the mean point of myDist
myOrigin = NumericalPoint(myDist.getMean())

# BEGIN_TEX
# Creation of a random walk
myRandomWalk = RandomWalk(myOrigin, myDist, myTimeGrid)
# END_TEX
