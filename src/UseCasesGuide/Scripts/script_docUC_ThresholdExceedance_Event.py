from __future__ import print_function
from openturns import *

# Create the model Y = x1 + 2*x2
model = NumericalMathFunction(["x1", "x2"], ["y"], ["x1+2*x2"])

# Create the input distribution and random vector X
inputDist = ComposedDistribution([Normal(), Normal()], IndependentCopula(2))
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
output = RandomVector(model, inputVector)

# To have a beautifull graph of importance factors,
# give the output random variable a name
output.setName("MyOutputY")

# BEGIN_TEX
# Create the event Y > 4
threshold = 4
myEvent = Event(output, Greater(), threshold)

#  Build a standard event based on an event
myStandardEvent2 = StandardEvent(myEvent)
# END_TEX
