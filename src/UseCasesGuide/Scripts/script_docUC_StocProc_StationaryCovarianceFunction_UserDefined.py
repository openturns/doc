from __future__ import print_function
from openturns import *

# We detail the example described in the documentation
# Create the time grid
t0 = 0.0
dt = 0.5
N = int((20.0 - t0) / dt)
myShiftMesh = RegularGrid(t0, dt, N)

# Create the covariance function


def gamma(tau):
    return 1.0 / (1.0 + tau * tau)

# Create the collection of HermitianMatrix
myCovarianceCollection = CovarianceMatrixCollection()
for k in range(N):
    t = myShiftMesh.getValue(k)
    matrix = CovarianceMatrix(1)
    matrix[0, 0] = gamma(t)
    myCovarianceCollection.add(matrix)

# One vertex of the mesh
tau = 1.5

# BEGIN_TEX
# Create the covariance model
myCovarianceModel = UserDefinedStationaryCovarianceModel(
    myShiftMesh, myCovarianceCollection)

# Get the covariance function computed at the vertex tau
myCovarianceMatrix = myCovarianceModel(tau)
# END_TEX

# Graph of the spectral function
x = NumericalSample(N, 2)
for k in range(N):
    t = myShiftMesh.getValue(k)
    x[k, 0] = t
    value = myCovarianceModel(t)
    x[k, 1] = value[0, 0]

# Create the curve of the spectral function
myCurve = Curve(x, 'UserModel')

# Create the graph
myGraph = Graph('User covariance model', 'Time', 'Covariance function', True)
myGraph.add(myCurve)
myGraph.setLegendPosition('topright')
# Show(myGraph)
