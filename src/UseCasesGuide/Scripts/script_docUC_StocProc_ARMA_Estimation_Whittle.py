from __future__ import print_function
from openturns import *

# Create the RegularGrid
tMin = 0.
timeStep = 0.1
n = 1000
myTimeGrid = RegularGrid(tMin, timeStep, n)

# Create the distribution of dimension 1
# Care : the mean must be NULL
myDist_1 = Triangular(-1., 0.0, 1.)

# Create  a white noise of dimension 1
myWN_1d = WhiteNoise(myDist_1, myTimeGrid)

# Create the ARMA model : ARMA(4,2) in dimension 1
myARCoef = ARMACoefficients(NumericalPoint([0.4, 0.3, 0.2, 0.1]))
myMACoef = ARMACoefficients(NumericalPoint([0.4, 0.3]))
myARMA = ARMA(myARCoef, myMACoef, myWN_1d)

# Create a time series from the process
myTimeSeries = myARMA.getRealization()

# Create a sample of N time series from the process
N = 100
myProcessSample = myARMA.getSample(N)

# BEGIN_TEX
###################################
# CASE 1 : we specify a (p,q) order
###################################

# Specify the order (p,q)
p = 4
q = 2

# Build a Whittle factory
# with default SpectralModelFactory (WelchFactory)
myFactory_42 = WhittleFactory(p, q)

# Check the default SpectralModelFactory
print("Default Spectral Model Factory = ",
      myFactory_42.getSpectralModelFactory())

# To set the spectral model factory
# For example, set WelchFactory as SpectralModelFactory
# with the Hanning filtering window
# The Welch estimator splits the time series in four blocs without overlap
myFilteringWindow = Hanning()
mySpectralFactory = WelchFactory(myFilteringWindow, 4, 0)
myFactory_42.setSpectralModelFactory(mySpectralFactory)
print("The new Spectral Model Factory = ",
      myFactory_42.getSpectralModelFactory())

###################################
# CASE 2 : we specify a range of (p,q) orders
###################################

# Range for p = [1, 2, 4]
pIndices = Indices([1, 2, 4])
# Range for q = [4,5,6]
qIndices = Indices(3)
# fill form 4 by step = 1
qIndices.fill(4, 1)

# Build a Whittle factory with default SpectralModelFactory (WelchFactory)
# this time using ranges of order p and q
myFactory_Range = WhittleFactory(pIndices, qIndices)

###################################
# Coefficients estimation
###################################

# Estimate the ARMA model from a time series
# To get the quantified AICc, AIC and BIC criteria
myCriterion = NumericalPoint()

myARMA_42 = myFactory_42.build(TimeSeries(myTimeSeries), myCriterion)

# Estimate the arma model from a process sample
myARMA_Range = myFactory_Range.build(myProcessSample, myCriterion)


###################################
# Results exploitation
###################################

# Get the white noise of the (best) estimated arma
myWhiteNoise = myARMA_Range.getWhiteNoise()

# When specified, get the quantified criterion
# for the best model
print("Criteria AICc = ", myCriterion[0])
print("Criteria AIC = ", myCriterion[1])
print("Criteria BIC = ", myCriterion[2])

# Get all the estimated models
myWhittleHistory = myFactory_Range.getHistory()

# Print the all the models and the criterion in the history
for i in range(myWhittleHistory.getSize()):
    model_i = myWhittleHistory[i]
    arma = model_i.getARMA()
    print("Order(p,q) = ",  model_i.getP(), ", ", model_i.getQ())
    print("AR coeff = ", model_i.getARCoefficients())
    print("MA coeff = ", model_i.getMACoefficients())
    print("White Noise - Sigma = ", model_i.getSigma2())
    print("Criteria AICc, AIC, BIC = ", model_i.getInformationCriteria())
    print('')
    # END_TEX
