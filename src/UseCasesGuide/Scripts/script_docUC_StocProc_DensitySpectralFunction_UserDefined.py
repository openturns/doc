from __future__ import print_function
from openturns import *
from math import exp

# Example described in the Use Cases Guide

# Create the frequency grid
fmin = 0.1
df = 0.2
N = int((10.0 - fmin) / df)
myFrequencyGrid = RegularGrid(fmin, df, N)

# Spectral function


def s(f):
    if(f <= 5.0):
        return 1.0
    else:
        x = f - 5.0
        return exp(-2.0 * x * x)

# Create the collection of HermitianMatrix
myCollection = HermitianMatrixCollection()
for k in range(N):
    frequency = myFrequencyGrid.getValue(k)
    matrix = HermitianMatrix(1)
    matrix[0, 0] = s(frequency)
    myCollection.add(matrix)


# BEGIN_TEX
# Create the spectral model
mySpectralModel = UserDefinedSpectralModel(myFrequencyGrid, myCollection)

# Get the spectral density function computed at first frequency values
firstFrequency = myFrequencyGrid.getStart()
frequencyStep = myFrequencyGrid.getStep()
myFirstHermitian = mySpectralModel(firstFrequency)

# Get the spectral function at frequency + 0.3 * frequencyStep
mySpectralModel(frequency + 0.3 * frequencyStep)

# END_TEX

# Graph of the spectral function
x = NumericalSample(N, 2)
for k in range(N):
    frequency = myFrequencyGrid.getValue(k)
    x[k, 0] = frequency
    value = mySpectralModel(frequency)
    x[k, 1] = value[0, 0].real

# Create the curve of the spectral function
myCurve = Curve(x, 'UserSpectral')

# Create the graph
myGraph = Graph('Spectral user', 'Frequency', 'Spectral density value', True)
myGraph.add(myCurve)
myGraph.setLegendPosition('topright')

# Draw the graph
#myGraph.draw('UserDefinedSpectralModelDemonstration', 800, 600, GraphImplementation.PNG)
