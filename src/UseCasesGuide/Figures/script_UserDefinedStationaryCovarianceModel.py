from openturns import *

# Create the time grid
t0 = 0.0
dt = 0.5
N = int((20.0 - t0)/ dt)
myTimeGrid =  RegularGrid(t0, dt, N)

# covariance function
def gamma(tau):
  return 1.0 / (1.0 + tau * tau)

# Create the collection of HermitianMatrix
myCollection = CovarianceMatrixCollection()
for k in range(N):
  t = myTimeGrid.getValue(k)
  matrix = CovarianceMatrix(1)
  matrix[0, 0] = gamma(t)
  myCollection.add(matrix)

# Create the covariance model
myStationaryCovariance = UserDefinedStationaryCovarianceModel(myTimeGrid, myCollection)

# Graph of the spectral function
x = NumericalSample(N, 2)
for k in range(N):
  t = myTimeGrid.getValue(k)
  x[k, 0] = t
  value = myStationaryCovariance.computeCovariance(t)
  x[k, 1] = value[0,0]

# Create the curve of the spectral function
myCurve = Curve(x, 'UserStationaryCovariance')

# Create the graph
myGraph = Graph('User covariance model', 'Time', 'Covariance function', True)
myGraph.add(myCurve)
myGraph.setLegendPosition('topright')

# Draw the graph
myGraph.draw('UserDefinedStationaryCovarianceModelDemonstration', 800, 600, GraphImplementation.PNG)
myGraph.draw('UserDefinedStationaryCovarianceModelDemonstration', 800, 600, GraphImplementation.PDF)
