from __future__ import print_function
from openturns import *

# Create a process: Omega * R^2 --> R^3

# Define a bi dimensional mesh
myIndices = Indices([40, 20])
myMesher = IntervalMesher(myIndices)
lowerBound = [0., 0.]
upperBound = [2., 1.]
myInterval = Interval(lowerBound, upperBound)
myMesh = myMesher.build(myInterval)


# Create the covariance model
# Amplitude and scale values of the Exponential model
amplitude = [1.0, 2.0, 3.0]
scale = [4.0, 5.0, 6.0]
# spatialCorrelation
spatialCorrelation = CorrelationMatrix(3)
spatialCorrelation[0, 1] = 0.8
spatialCorrelation[0, 2] = 0.6
spatialCorrelation[1, 2] = 0.1
myCovarianceModel = ExponentialModel(
    myMesh.getDimension(), amplitude, scale, spatialCorrelation)

# Create a normal process with the temporal view ONLY
myProcess = TemporalNormalProcess(myCovarianceModel, myMesh)


# Create a domain A in R^3
# for example: [0.8; 1.2]*[1.5; 1.6]*[0.5; 0.7]
lowerBound = NumericalPoint([0.8, 1.5, 0.5])
upperBound = NumericalPoint([1.2, 1.6, 0.7])
myDomainA = Interval(lowerBound, upperBound)

# BEGIN_TEX
myEvent = Event(myProcess, myDomainA)
# END_TEX
