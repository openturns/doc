from __future__ import print_function
from openturns import *

# Example in dimension 1
# Normal process with an Exponential covariance model

# Dimension parameter
dimension = 1

# Amplitude and scale values of the Exponential model
amplitude = NumericalPoint(dimension, 1.0)
scale = NumericalPoint(dimension, 1.0)

# Create the time grid
t0 = 0.0
N = 300
t1 = 20.0
dt = (t1 - t0) / N
myTimeGrid = RegularGrid(t0, dt, N)

# Create the covariance model
# for example : the Exponential model
# from the amplitude, scale and spatialCovariance
myCovarianceModel = ExponentialModel(
    myTimeGrid.getDimension(), amplitude, scale)

# Create a stationary Normal process with
# that covariance model
myProcess = TemporalNormalProcess(myCovarianceModel, myTimeGrid)

# Create a time series and a sample of time series
myTimeSeries = myProcess.getRealization()
mySample = myProcess.getSample(1000)

# Create a spectral factory
# for example : theelch allgorithm
# with the hanning window and N blocks
# with the default overlap size (=0.5)
mySegmentNumber = 5
mySpectralFactory = WelchFactory(Hanning(), mySegmentNumber)


# BEGIN_TEX
# Build a factory of stationary covariance function
myCovarianceFactory = StationaryCovarianceModelFactory()

# Set the spectral factory algorithm
myCovarianceFactory.setSpectralModelFactory(mySpectralFactory)

# Check the current spectral factory
print(myCovarianceFactory.getSpectralModelFactory())

#########################################
# Case 1 :  Estimation on a ProcessSample

# The spectral model factory computes the spectral density function
# without using the block and overlap arguments of the Welch factories
myEstimatedModel_PS = myCovarianceFactory.build(mySample)

#########################################
# Case 2 :  Estimation on a TimeSeries

# The spectral model factory compute the spectral density function using
# the block and overlap arguments of spectral model factories
myEstimatedModel_TS = myCovarianceFactory.build(myTimeSeries)

#########################################
# Manipulation of the estimated model

# Evaluate the covariance function at each time step
# Care : if estimated from a time series, the time grid has changed
for i in range(N):
    tau = myTimeGrid.getValue(i)
    cov = myEstimatedModel_PS(tau)
    # END_TEX

# Graph
myGraph = Graph(
    'Covariance estimation', 'time', 'Covariance value C(0,t)', True)

sampleT = NumericalSample(N, 1)
sampleValueEstimated = NumericalSample(N, 1)
sampleValueModel = NumericalSample(N, 1)
for i in range(N):
    t = myTimeGrid.getValue(i)
    sampleT[i, 0] = t
    for j in range(i - 1):
        s = myTimeGrid.getValue(j)
        estimatedValue = myEstimatedModel_PS(t, s)
        modelValue = myCovarianceModel(t, s)
        if (j == 0):
            sampleValueEstimated[i, 0] = estimatedValue[0, 0]
            sampleValueModel[i, 0] = modelValue[0, 0]

# Drawing...
myCurveEstimated = Curve(sampleT, sampleValueEstimated, 'Estimated model')
myGraph.add(myCurveEstimated)
myCurveModel = Curve(sampleT, sampleValueModel, 'Exact model')
myCurveModel.setColor('red')
myGraph.add(myCurveModel)
myGraph.setLegendPosition('topright')
myGraph.draw('StationaryCovarianceModelEstimation',
             800, 600,  GraphImplementation.PNG)
myGraph.draw('StationaryCovarianceModelEstimation',
             800, 600,  GraphImplementation.PDF)
