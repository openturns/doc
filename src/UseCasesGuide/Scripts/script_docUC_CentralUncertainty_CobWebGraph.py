from __future__ import print_function
from openturns import *

# Create the model Y = x1^2 + x2
model = NumericalMathFunction(["x1", "x2"], ["y"], ["x1^2+x2"])

# Create the input distribution and random vector X
myCorMat = CorrelationMatrix(2)
myCorMat[0, 1] = -0.6
inputDist = Normal([0., 0.], myCorMat)
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
output = RandomVector(model, inputVector)

# Generate the input sample
N = 500
inputSample = inputVector.getSample(N)

# Evaluate the associated output sample
outputSample = model(inputSample)
outputSample.setDescription("Y")

# BEGIN_TEX
####################################
# Graph 1 : value based scale to describe the Y range
####################################
minValue = 3
maxValue = 20
myCobweb = VisualTest.DrawCobWeb(
    inputSample, outputSample, minValue, maxValue, 'red', False)
# View(myCobweb).show()

####################################
# Graph 2 : rank based scale to describe the Y range
####################################
minValue = 0.9
maxValue = 1
myCobweb2 = VisualTest.DrawCobWeb(
    inputSample, outputSample, minValue, maxValue, 'red', True)
# View(myCobweb2).show()

# In order to increase the bounding box of the graph
bb = myCobweb2.getBoundingBox()
# define the incresaing factor of the bounding box
factor = 1.1
bb[1] = factor * bb[1]
myCobweb2.setBoundingBox(bb)

# Save in a PNG file
myCobweb2.draw('cobWeb', 640, 480, GraphImplementation.PNG)
# Save in any formats
myCobweb2.draw('cobWeb')

# END_TEX
