from __future__ import print_function
from openturns import *

# Create the time grid
# In the context of the spectral estimate or Fourier transform use,
# we use data blocs with size of form 2^p
tMin = 0.
timeStep = 0.1
size = pow(2, 12)
myTimeGrid = RegularGrid(tMin, timeStep, size)

# We fix the parameter of the Cauchy model
amplitude = NumericalPoint([5])
scale = NumericalPoint([3])
model = ExponentialCauchy(amplitude, scale)
myNormalProcess = SpectralNormalProcess(model, myTimeGrid)

# Get a time series or a sample of time series
myTimeSeries = myNormalProcess.getRealization()
mySample = myNormalProcess.getSample(1000)

mySegmentNumber = 10
myOverlapSize = 0.3

# BEGIN_TEX
# Build a spectral model factory
myFactory = WelchFactory(Hanning(), mySegmentNumber, myOverlapSize)

# Estimation on a TimeSeries or on a ProcessSample
myEstimatedModel_TS = myFactory.build(myTimeSeries)
myEstimatedModel_PS = myFactory.build(mySample)

# Change the filtering window
myFactory.setFilteringWindows(Hamming())

# Get the FFT algorithm
myFFT = myFactory.getFFTAlgorithm()

# Get the frequencyGrid
frequencyGrid = myEstimatedModel_PS.getFrequencyGrid()
# END_TEX


# With the model, we want to compare values
# We compare values computed with theoritical values
plotSample = NumericalSample(frequencyGrid.getN(), 3)

# Loop of comparison ==> data are saved in plotSample
for k in range(frequencyGrid.getN()):
    freq = frequencyGrid.getStart() + k * frequencyGrid.getStep()
    plotSample[k, 0] = freq
    plotSample[k, 1] = abs(myEstimatedModel_PS(freq)[0, 0])
    plotSample[k, 2] = abs(model.computeSpectralDensity(freq)[0, 0])


# Graph section
# We build 2 curves
# each one is function of frequency values
ind = Indices(2)
ind.fill()

# Some cosmetics : labels, legend position, ...
graph = Graph("Estimated spectral function - Validation", "Frequency",
              "Spectral density function", True, "topright", 1.0, GraphImplementation.LOGY)

# The first curve is the estimate density as function of frequency
curve1 = Curve(plotSample.getMarginal(ind))
curve1.setColor('blue')
curve1.setLegend('estimate model')

# The second curve is the theoritical density as function of frequency
ind[1] = 2
curve2 = Curve(plotSample.getMarginal(ind))
curve2.setColor('red')
curve2.setLegend('Cauchy model')

graph.add(curve1)
graph.add(curve2)

# Finally we draw
graph.draw('welchValidation', 800, 600,  GraphImplementation.PNG)
