from __future__ import print_function
from openturns import *

# Create a mesh which is a RegularGrid
tMin = 0.0
timeStep = 0.1
n = 100
myTimeGrid = RegularGrid(tMin, timeStep, n)

# Create  a process  of dimension 3
# Normal process with an Exponential covariance model
# Amplitude and scale values of the Exponential model
amplitude = [1.0, 2.0, 3.0]
scale = [4.0]
# spatialCorrelation
spatialCorrelation = CorrelationMatrix(3)
spatialCorrelation[0, 1] = 0.8
spatialCorrelation[0, 2] = 0.6
spatialCorrelation[1, 2] = 0.1
myCovarianceModel = ExponentialModel(
    myTimeGrid.getDimension(), amplitude, scale, spatialCorrelation)
myProcess = TemporalNormalProcess(myCovarianceModel, myTimeGrid)


# BEGIN_TEX
# Get the dimension d of the process
dimension = myProcess.getDimension()

# Get the mesh of the process
myMesh = myProcess.getMesh()

# Get the time grid of the process
# only when the mesh can be interpreted as a regular time grid
myTimeGrid = myProcess.getTimeGrid()

# Get a realisation of the process
myField = myProcess.getRealization()

# Get several realisations of the process
number = 10
myFieldSample = myProcess.getSample(number)

# Get a continuous realisation of the process
myContReal = myProcess.getContinuousRealization()

# Get its first marginal
myContReal_marg1 = myContReal.getMarginal(0)
# Get the corners of the mesh
minMesh = myMesh.getVertices().getMin()
maxMesh = myMesh.getVertices().getMax()
myGraph = myContReal_marg1.draw(minMesh[0], maxMesh[0])
# Show(myGraph)

# Get the marginal of the process at index 1
# Care! Numerotation begins at 0
# Not yet implemented for some processes
# myMarginalProcess = myProcess.getMarginalProcess(1)

# Get the marginal of the process at index in indices
# Not yet implemented for some processes
# indices = Indices([0, 1])
# myMarginalProcess_2D = myProcess.getMarginalProcess(indices)

# Check  wether the process is normal
print(myProcess.isNormal())

# Check  wether the process is stationary
print(myProcess.isStationary())
# END_TEX
