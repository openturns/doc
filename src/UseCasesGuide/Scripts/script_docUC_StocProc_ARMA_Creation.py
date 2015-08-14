from __future__ import print_function
from openturns import *

# Create the RegularGrid
tMin = 0.
timeStep = 0.1
n = 100
myTimeGrid = RegularGrid(tMin, timeStep, n)

# Create the distribution of dimension 1
# Care : the mean must be NULL
myDist_1 = Triangular(-1.0, 0.0, 1.0)

# Create  a white noise of dimension 1
myWN_1d = WhiteNoise(myDist_1, myTimeGrid)

# Create the list of coefficients
# ARMA(4,2) in dimension 1
myARList = NumericalPoint([0.4, 0.3, 0.2, 0.1])
myMAList = NumericalPoint([0.4, 0.3])

# Define the last state of the ARMA
myLastValues = NumericalSample([[0.6], [0.7], [0.3], [0.2]])
myLastNoiseValues = NumericalSample([[1.2], [1.8]])

# BEGIN_TEX
#####################################
# CASE 1 : Whithout specifying the current state
#####################################

# Create the AR and MA coefficients

# From the lists of the coefficeints
# which are vectors in dimension 1 and
# square matrix in dimension d>1
myARCoef = ARMACoefficients(myARList)
myMACoef = ARMACoefficients(myMAList)


# Create the ARMA model

# From the ARMA coefficients, the white noise
# whithout specifying the current state
myARMA = ARMA(myARCoef, myMACoef, myWN_1d)


#####################################
# CASE 2 : Specifying the current state
# Usefull to get possible futurs from the current state
#####################################

# Define the current state of the ARMA

# Set the last p-values of the process
# and the last q-values of the noise
myARMAState = ARMAState(myLastValues, myLastNoiseValues)


# Create the ARMA model

# From the AR-MA coefficients, the white noise and a specific state
myARMA = ARMA(myARCoef, myMACoef, myWN_1d, myARMAState)
# END_TEX
