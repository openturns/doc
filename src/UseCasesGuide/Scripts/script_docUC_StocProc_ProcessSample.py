from __future__ import print_function
from openturns import *

# Define a bi dimensional mesh as a box
myIndices = Indices([100, 40])
myMesher = IntervalMesher(myIndices)
lowerBound = [0., 0.]
upperBound = [2., 1.]
myInterval = Interval(lowerBound, upperBound)
myMesh = myMesher.build(myInterval)


# Create a second order normal porcess of dimension 3
# We use the Cauchy model
amplitude = NumericalPoint([5])
scale = NumericalPoint([3]*2)
model = ExponentialModel(myMesh.getDimension(), amplitude, scale)
myProcess = TemporalNormalProcess(model, myMesh)

# Get a field
myField = myProcess.getRealization()
myField_2 = myProcess.getRealization()

# Get a process sample of size 10
mySampleFields = myProcess.getSample(10)

# BEGIN_TEX
############################
# Case 1: Create a process sample
# by duplicating the same field
number = 10
myProcessSample_1 = ProcessSample(number, myField)

############################
# Case 1: Create a process sample of size 10
# from a process
myProcessSample = myProcess.getSample(10)

# Add a field to the process sample
myProcessSample.add(myField)

# Get the field of index i=2
myFieldIndexI = myProcessSample[2]

# Compute the  mean of the process sample
# The result is a field
myMeanField = myProcessSample.computeMean()

# Compute the spatial mean of the process sample
# The result is a numerical sample
myMeanNS = myProcessSample.computeSpatialMean()

# Compute the quantiles per component associated to the level q
# The result is a field
q = 0.50
myQuantileField = myProcessSample.computeQuantilePerComponent(q)
# END_TEX
