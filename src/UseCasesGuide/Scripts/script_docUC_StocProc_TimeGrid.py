from __future__ import print_function
from openturns import *

# Create a time grid

# BEGIN_TEX
# Define the lower bound of the time grid, the number of steps
# and the time step between two instants

tMin = 0.
timeStep = 0.1
n = 10

# Create the RegularGrid
myRegularGrid = RegularGrid(tMin, timeStep, n)

# Get the first and the last instants,
# the step and the number of points of a RegularGrid
myMin = myRegularGrid.getStart()
myMax = myRegularGrid.getEnd()
myStep = myRegularGrid.getStep()
myRegularGridSize = myRegularGrid.getN()
# END_TEX
