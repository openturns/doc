from __future__ import print_function
from openturns import *

# Create the RegularGrid
tMin = 0.
timeStep = 0.1
N = 100
myTimeGrid = RegularGrid(tMin, timeStep, N)

# Create the values of the time series
# here we gert the numerical sample from a particular process
# build on the same time grid
# White noise of dmension 3
myProcess = WhiteNoise(Normal(3), myTimeGrid)

ts = myProcess.getRealization()
myValues = ts.getSample()

# BEGIN_TEX
###########################
# Case 1: Create a time series from a time grid and values
# Care! The number of steps of the time grid must correspond to the size
# of the values
myTimeSeries = TimeSeries(myTimeGrid, myValues)


###########################
# Case 2: Get a time series from the process myProcess
myTimeSeries2 = myProcess.getRealization()

# Get the number of values of the time series
print('Dimension = ', myTimeSeries.getSize())

# Get the dimension of the values observed at each time
print('Dimension = ', myTimeSeries.getDimension())

# Get the value Xi at index i
# Care! Numerotation begins at i=0
i = 37
print('Xi = ', myTimeSeries.getValueAtIndex(i))

# Get the value Xi of the observed time series at time
# the nearest of myTime
myTime = 3.4
print('Xi at time the nearest of myTime',
      myTimeSeries.getValueAtNearestTime(myTime))

# Get the time series at index i : (ti, Xi)
i = 37
print('(ti, Xi) = ', myTimeSeries[i])

# Get a the marginal value at index i of the time series
i = 37
# get the time stamp:
print('ti = ', myTimeSeries[i, 0])
# get the first component of the corresponding value :
print('Xi1 = ', myTimeSeries[i, 1])

# Get all the values (X1, .., Xn) of the time series
allValues = myTimeSeries.getSample()

# Compute the temporal Mean
# It corresponds to the mean of the values of the time series
myTemporalMean = myTimeSeries.getTemporalMean()

# Draw the marginal i of the time series
# Care! Numerotation begins at i=0
# using linear interpolation
myMarginalTimeSerie = myTimeSeries.drawMarginal(0)
# Show(myMarginalTimeSerie)

# with no interpolation
myMarginalTimeSerie2 = myTimeSeries.drawMarginal(0, False)
# Show(myMarginalTimeSerie2)
# END_TEX
