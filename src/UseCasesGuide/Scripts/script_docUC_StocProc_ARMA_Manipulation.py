from __future__ import print_function
from openturns import *

# Create the RegularGrid
tMin = 0.
timeStep = 0.1
n = 100
myTimeGrid = RegularGrid(tMin, timeStep, n)

# Create the distribution of dimension 1 or 3
# Care : the mean must be NULL
myDist_1 = Triangular(-1., 0.0, 1.)

# Create  a white noise of dimension 1
myWN_1d = WhiteNoise(myDist_1, myTimeGrid)

# Create the ARMA model : ARMA(4,2) in dimension 1
myARCoef = ARMACoefficients(NumericalPoint([0.4, 0.3, 0.2, 0.1]))
myMACoef = ARMACoefficients(NumericalPoint([0.4, 0.3]))
myARMA = ARMA(myARCoef, myMACoef, myWN_1d)

# BEGIN_TEX
# Check the linear recurrence
print("myARMA = ", myARMA)

# Get the coefficients of the recurrence
print('AR coeff = ', myARMA.getARCoefficients())
print('MA coeff = ', myARMA.getMACoefficients())

# Get the white noise
myWhiteNoise = myARMA.getWhiteNoise()

# Generate one time series
ts = myARMA.getRealization()
ts.setName('my time series')

# Draw the time series  : marginal index 0
myTSGraph = ts.drawMarginal(0)
# View(myTSGraph).show()

# Generate a k time series
k = 5
myProcessSample = myARMA.getSample(k)

# Then get the current state of the ARMA
myARMAState = myARMA.getState()
# From the myARMAState, get the last values
myLastValues = myARMAState.getX()
# From the ARMAState, get the last noise values
myLastEpsilonValues = myARMAState.getEpsilon()

# Get the number of iterations before getting a stationary state
nThermal = myARMA.getNThermalization()
print('Thermalization number = ', nThermal)

# This may be important to evaluate it  with another precision epsilon
epsilon = 1e-8
newThermalValue = myARMA.computeNThermalization(epsilon)
myARMA.setNThermalization(newThermalValue)

# Make a prediction from the curent state of the ARMA
# on the next Nit instants
Nit = 100
# at first, specify a current state myARMAState
myARMA = ARMA(myARCoef, myMACoef, myWhiteNoise, myARMAState)

# then, generate a possible future
possibleFuture = myARMA.getFuture(Nit)

# Generate N possible futures on the Nit next points
N = 5
possibleFuture_N = myARMA.getFuture(Nit, N)
possibleFuture_N.setName('Possible futures')

# Draw the future  : marginal index 0
myFutureGraph = possibleFuture_N.drawMarginal(0)
# View(myFutureGraph).show()
# END_TEX
