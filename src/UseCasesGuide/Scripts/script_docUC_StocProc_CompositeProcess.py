from __future__ import print_function
from openturns import *

##########################################
# Create a spatial  dynamical function
# Create the function g : R^2 --> R^2
#               (x1,x2) --> (x1^2, x1+x2)
g = NumericalMathFunction(['x1', 'x2'],  ['x1^2', 'x1+x2'])

# Convert g : R --> R into a spatial fucntion
# n is the dimension of the mesh
# of the field on wich g will be applied
nSpat = 2
myDynFunc = SpatialFunction(g, nSpat)

# Then g acts on processes X: Omega * R^nSpat --> R^2


##########################################
# Create a trend function fTrend: R^n --> R^q
# for example for  myXtProcess of dimension 2
# defined on a bidimensional mesh
# fTrend : R^2 --> R^2
#          (t1, t2) --> (1+2t1, 1+3t2)
fTrend = NumericalMathFunction(["t1", "t2"], ["1+2*t1", "1+3*t2"])


##########################################
# Create a normal process of dimension 2
# which mesh is of box of dimension 2

myIndices = Indices([80, 40])
myMesher = IntervalMesher(myIndices)
lowerBound = [0., 0.]
upperBound = [2., 1.]
myInterval = Interval(lowerBound, upperBound)
myMesh = myMesher.build(myInterval)

# Define a bidimensional temporal normal process on the mesh
# with independent components
amplitude = [1.0, 1.0]
scale = [0.2, 0.3]
myCovModel = ExponentialModel(myMesh.getDimension(), amplitude, scale)

myXtProcess_temp = TemporalNormalProcess(myCovModel, myMesh)

# Non linear transformation of myXtProcess
# to get a positive process
g2 = NumericalMathFunction(['x1', 'x2'],  ['x1^2', 'abs(x2)'])
myDynTransform = SpatialFunction(g2, 2)
myXtProcess = CompositeProcess(myDynTransform, myXtProcess_temp)

# BEGIN_TEX
#######################
# Case 1 : General case
#######################

# Create the  image Y
myYtProcess = CompositeProcess(myDynFunc, myXtProcess)

# Get the antecedent : myXtProcess
print('My antecedent process = ', myYtProcess.getAntecedent())

# Get the dynamical function
# which performs the transformation
print('My dynamical function = ', myYtProcess.getFunction())


##############################
# Case 2 : Addition of a trend
##############################

# Create the temporal function fTemp
# from the function fTrend
fTemp = TrendTransform(fTrend)

# Create the composite process
# myYtProcess_trend = myXtProcess + fTrend(t)
myYtProcess_trend = CompositeProcess(fTemp, myXtProcess)

#################################
# Case 3 : Box Cox transformation
#################################

# Create a Box Cox transformation
# for example for a process of dimension 2
# fBoxCox : R^2 --> R^1
#            (x1,x2) --> (log(x1),log(x2))
# fSpat will be applied on process with bidimensional mesh
n = 2
fSpat = SpatialFunction(BoxCoxTransform([0.0, 0.0]), n)

# Create the process
# myYtProcesss_boxcox = BoxCoxTransform(myXtProcess)
myYtProcess_boxcox = CompositeProcess(fSpat, myXtProcess)

# END_TEX
