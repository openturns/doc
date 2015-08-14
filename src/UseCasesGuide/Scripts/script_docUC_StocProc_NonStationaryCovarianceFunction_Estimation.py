from __future__ import print_function
from openturns import *
from math import *
from time import time

# We create a non stationary normal process :
# myProcess: Omega * [0,T]  --> R


# Create the covariance function at (s,t)

def C(s, t):
    return exp(-4.0 * abs(s - t) / (1 + (s * s + t * t)))


# Create the time grid
t0 = -4.0
tmax = 4.0
N = 64
dt = (tmax - t0) / N
myMesh = RegularGrid(t0, dt, N)

# Create the collection of HermitianMatrix
myCovarianceCollection = CovarianceMatrixCollection()
for k in range(N):
    s = myMesh.getValue(k)
    for l in range(k + 1):
        t = myMesh.getValue(l)
        matrix = CovarianceMatrix(1)
        matrix[0, 0] = C(s, t)
        myCovarianceCollection.add(matrix)

# Create the covariance model
myCovarianceModel = UserDefinedCovarianceModel(myMesh, myCovarianceCollection)

# Create the normal process with that covariance model
# based on the  mesh myMesh
myProcess = TemporalNormalProcess(myCovarianceModel, myMesh)

# Get a sample of fields from the process
N = 1000
myFieldSample = myProcess.getSample(N)

# BEGIN_TEX
# Build a covariance model factory
myFactory = NonStationaryCovarianceModelFactory()

# Estimation on a the ProcessSample
myEstimatedModel = myFactory.build(myFieldSample)

# END_TEX
