from openturns import *
from math import *
from time import time

# We create a non stationary normal process :
# myProcess: Omega * R  --> R


# Create the covariance function at (s,t)

def C(s, t):
  return exp( -4.0 * abs(s - t) / (1 + (s * s + t * t)))

def covModRef(X):
  return [C(X[0], X[1])]

myFuncCovarianceRef = PythonFunction(2, 1, covModRef)
myFuncCovarianceRef.setDescription(["s", "t", "C"])

t0 = -4.0
tmax = 4.0

# Draw the isocontours of the discretized covariance function
print "draw the reference"
myGraphRef = myFuncCovarianceRef.draw([t0, t0], [tmax, tmax])
alld = myGraphRef.getDrawables()
levels = NumericalPoint(alld.getSize())
for i in range(alld.getSize()):
  d = alld[i]
  d.setLineStyle("twodash")
  d.setLineWidth(2)
  myGraphRef.setDrawable(d, i)
  levels[i] = d.getLevels()[0]

# Create the time grid
for iN in range(2, 11):
  t_00 = time()
  N = 2**iN
  print "N=", N
  dt = (tmax - t0) / N
  myMesh =  RegularGrid(t0, dt, N)

  # Keep only time stamps in the time-grid
  tmax = myMesh.getEnd()

  # Create the collection of HermitianMatrix
  print "Create the covariance matrices"
  myCovarianceCollection = CovarianceMatrixCollection()
  index = 0
  for k in range(N):
    s = myMesh.getValue(k)
    for l in range(k+1):
      t = myMesh.getValue(l)
      matrix = CovarianceMatrix(1)
      matrix[0, 0] = C(s, t)
      index += 1
      myCovarianceCollection.add(matrix)

  # Create the covariance model
  myCovarianceModel = UserDefinedCovarianceModel(myMesh, myCovarianceCollection)

  # Create the non stationary Normal process with
  # that covariance model
  print "create the process"
  myProcess = TemporalNormalProcess(myCovarianceModel, myMesh)

  # Create a  sample of fields
  for isize in range(1, 7):
    t_0 = time()
    size = 10**isize
    print "generate the sample, size=", size
    myFieldSample = myProcess.getSample(size)

    # Build a covariance model factory
    myFactory = NonStationaryCovarianceModelFactory()

    # Estimation on a the ProcessSample
    print "estimate the covariance"
    myEstimatedModel = myFactory.build(myFieldSample)

    # Define the python function associated to myCovarianceModel
    def covMod(X):
      return [myEstimatedModel(X[0], X[1])[0, 0]]

    myFuncCovariance = PythonFunction(2, 1, covMod)

    print "draw the estimate"
    alld = myFuncCovariance.draw([t0, t0], [tmax, tmax]).getDrawables()
    myGraph = Graph(myGraphRef)
    for i in range(alld.getSize()):
      d = alld[i]
      d.setLegend("")
      d.setLevels([levels[i]])
      d.setDrawLabels(False)
      myGraph.add(d)
      print "generate file"
      myGraph.draw('NonStatCovFuncEstim_N' + str(N).zfill(4) + "_S" + str(size).zfill(7), 800, 600, GraphImplementation.PDF)
      print "N=", N, "size=", size, "t=", time() - t_0, "s"
      print "N=", N, "t=", time() - t_00, "s"
