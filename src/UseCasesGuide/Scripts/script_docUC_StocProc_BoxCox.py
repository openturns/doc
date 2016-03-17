from __future__ import print_function
from openturns import *

# Create a process X: R^2 --> R^2

# Define a bi dimensional mesh as a box
myIndices = Indices([40, 20])
myMesher = IntervalMesher(myIndices)
lowerBound = [0., 0.]
upperBound = [2., 1.]
myInterval = Interval(lowerBound, upperBound)
myMesh = myMesher.build(myInterval)


# Define a scalar temporal normal process on the mesh
# this process is stationary
# myXproc R^2 --> R
amplitude = [1.0]
scale = [0.2]*2
myCovModel = ExponentialModel(myMesh.getDimension(), amplitude, scale)
myXproc = TemporalNormalProcess(myCovModel, myMesh)

# Transform myXproc to make its variance depend on the vertex (s,t)
# and to get a positive process
# thanks to the spatial function g
# myXtProcess R --> R
g = NumericalMathFunction(['x1'],  ['exp(x1)'])
myDynTransform = SpatialFunction(g, 2)
myXtProcess = CompositeProcess(myDynTransform, myXproc)

myField = myXtProcess.getRealization()

# BEGIN_TEX
################################
# CASE 1 : we estimate the Box Cox transformation from the data
################################

# Initiate a BoxCoxFactory
myBoxCoxFactory = BoxCoxFactory()

# We estimate the lambda parameter from the field myField
# In dimension upper than one, the estimate is done marginal by marginal
# We suppose here that all values of the field are positive
myModelTransform = myBoxCoxFactory.build(myField)
print(myModelTransform)

# Get the estimated lambda
estimatedLambda = myModelTransform.getLambda()

################################
# CASE 2 : we impose the Box Cox transformation
################################

# It is possible to impose the lambda factor myLambda
# for example in dimension 1
myLambda = 0.01
myModelTransform_lambda = BoxCoxTransform(myLambda)

################################
# Get the statibilized field

# Apply the transform method to myField
# myStabilizedField = h(myField) or h(myField + alpha)
myStabilizedField = myModelTransform(myField)
myStabilizedField.setName('Stabilized TS')

# Get the inverse of the Box Cox transformation
myInverseModelTransform = myModelTransform.getInverse()

# Apply it to the time series myFinalTimeSeries
# myInitialField = h^-1(myFinalField) or h^-1(myFinalField) - alpha
myInitialField = myInverseModelTransform(myStabilizedField)
# END_TEX

# export to VTK file each graph
myField.exportToVTKFile('myField.vtk')
myStabilizedField.exportToVTKFile('myStabilizedField.vtk')
