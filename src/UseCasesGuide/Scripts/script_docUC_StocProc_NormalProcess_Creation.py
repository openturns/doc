from __future__ import print_function
from openturns import *

# Example in dimension 3
# Normal process with an Exponential covariance model

# Create a trend function
# fTrend : R^2 --> R^3
#          (t,s) --> (1+2*t, 1+2*s, 1+2*s+2*t)
funcTrend = NumericalMathFunction(["t", "s"], ["1+2*t", "1+2*s", "1+2*s+2*t"])
print(funcTrend.__repr__())
print(funcTrend.getInputDimension())
myTrend = TrendTransform(funcTrend)
print(myTrend.__repr__())
print(myTrend.getInputDimension())
# Amplitude and scale values of the Exponential model
amplitude = [1., 2., 3.]
scale = [4., 5., 6.]

# spatialCorrelation
spatialCorrelation = CorrelationMatrix(3)
spatialCorrelation[0, 1] = 0.8
spatialCorrelation[0, 2] = 0.6
spatialCorrelation[1, 2] = 0.1


# Create a time grid
t0 = 0.0
dt = 0.1
size = 20
myTimeGrid = RegularGrid(t0, dt, size)


# Define a bi dimensional mesh
myIndices = Indices([40, 20])
myMesher = IntervalMesher(myIndices)
lowerBound = [0., 0.]
upperBound = [2., 1.]
myInterval = Interval(lowerBound, upperBound)
myMesh = myMesher.build(myInterval)


# Create the covariance model
# for example : the Exponential model
# from the amplitude, scale and spatialCovariance
myCovarianceModel = ExponentialModel(
    myMesh.getDimension(), amplitude, scale, spatialCorrelation)

# Create the spectral model
# for example : the Cauchy model
mySpectralModel = CauchyModel(amplitude, scale, spatialCorrelation)

# Create the second order model
# for example : the Exponential Cauchy model
mySecondOrderModel = ExponentialCauchy(amplitude, scale, spatialCorrelation)


# BEGIN_TEX
####################################
# CASE 1 : the normal process is defined by its temporal covariance
# function ONLY

# Create a normal process with the temporal view ONLY
myTempNormProc1 = TemporalNormalProcess(myTrend, myCovarianceModel, myMesh)


####################################
# CASE 2 : the normal process is defined by its spectral density function ONLY
# Stationary process ONLY
# Care! The mesh must be a time grid (n=1)

# Create a normal process with the spectral view ONLY
mySpectNormProc1 = SpectralNormalProcess(mySpectralModel, myTimeGrid)


##########################################################################
# CASE 3 : the normal process is defined by a second order that contains both the temporal covariance function and the associated spectral density function
# Stationary process ONLY
# Care! The mesh must be a time grid (n=1)

# Create the normal process to use its temporal properties
myTempNormProc2 = TemporalNormalProcess(mySecondOrderModel, myTimeGrid)

# Create the normal process to use its spectral properties
mySpectNormProc2 = SpectralNormalProcess(mySecondOrderModel, myTimeGrid)

# END_TEX
