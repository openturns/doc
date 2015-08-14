from __future__ import print_function
from openturns import *
from math import *

# Create the time grid
t0 = -4.0
tmax = 4.0
N = 64
dt = (tmax - t0) / N
myMesh = RegularGrid(t0, dt, N)

# Create the covariance function at (s,t)


def gamma(s, t):
    return exp(-4.0 * abs(s - t) / (1 + (s * s + t * t)))

# Create the collection of HermitianMatrix
myCovarianceCollection = CovarianceMatrixCollection()
for k in range(N):
    s = myMesh.getValue(k)
    for l in range(k + 1):
        t = myMesh.getValue(l)
        matrix = CovarianceMatrix(1)
        matrix[0, 0] = gamma(s, t)
        myCovarianceCollection.add(matrix)

# Instants of the time grid
s = 1.5
t = 2.5


# BEGIN_TEX
# Create the covariance model
myCovarianceModel = UserDefinedCovarianceModel(myMesh, myCovarianceCollection)

# Get the covariance function computed at (s,t)
# for example (1.5, 2.5)
s = 1.5
t = 2.5
# END_TEX

# Define the python function associated to myCovarianceModel


def covMod(X):
    return [myCovarianceModel(X[0], X[1])[0, 0]]


def covModRef(X):
    return [gamma(X[0], X[1])]

myFuncCovariance = PythonFunction(2, 1, covMod)
myFuncCovarianceRef = PythonFunction(2, 1, covModRef)
myFuncCovarianceRef.setDescription(["s", "t", "C"])

# Draw the isocontours of the discretized covariance function
# the ref model
myGraph = myFuncCovarianceRef.draw([t0 - 1, t0 - 1], [tmax + 1, tmax + 1])
alld = myGraph.getDrawables()
levels = NumericalPoint(alld.getSize())
for i in range(alld.getSize()):
    d = alld[i]
    d.setLineStyle("twodash")
    d.setLineWidth(2)
    myGraph.setDrawable(d, i)
    levels[i] = d.getLevels()[0]

# the discretized model
alld = myFuncCovariance.draw([t0, t0], [tmax, tmax]).getDrawables()
for i in range(alld.getSize()):
    d = alld[i]
    d.setLegend("")
    d.setLevels([levels[i]])
    d.setDrawLabels(False)
    myGraph.add(d)

# Show(myGraph)
#myGraph.draw('NonStationCovFunc', 600, 600, GraphImplementation.PDF)
