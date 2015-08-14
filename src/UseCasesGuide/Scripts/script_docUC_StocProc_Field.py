from __future__ import print_function
from openturns import *


# Define a bi dimensional mesh
myIndices = Indices([40, 20])
myMesher = IntervalMesher(myIndices)
lowerBound = [0., 0.]
upperBound = [2., 1.]
myInterval = Interval(lowerBound, upperBound)
myMesh = myMesher.build(myInterval)

# Define a scalar temporal normal process on the mesh
amplitude = [1.0]
scale = [0.2]
myCovModel = ExponentialModel(myMesh.getDimension(), amplitude, scale)

myProcess = TemporalNormalProcess(myCovModel, myMesh)
myValues = myProcess.getRealization().getValues()

# BEGIN_TEX
###########################
# Case 1: Create a field from a mesh and some values
myField = Field(myMesh, myValues)

###########################
# Case 2: Get a field from the process myProcess
myField2 = myProcess.getRealization()

# Get all the values of the field
myGeneratedValues = myField.getValues()

# Get the value of the field at the vertex i
i = 1
myValue_i = myGeneratedValues[i]

# Compute the spatial mean of the field
mySpatMean = myField.getSpatialMean()

# Draw the field without interpolation
myGraph1 = myField.drawMarginal(0, False)
# Show(myGraph1)

# Draw the field with interpolation
myGraph2 = myField.drawMarginal(0)
# Show(myGraph2)

# Export to the VTK format
myField.exportToVTKFile('myFile.vtk')
# END_TEX
