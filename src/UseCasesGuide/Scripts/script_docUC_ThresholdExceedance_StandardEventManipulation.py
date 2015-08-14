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
output.setName("MyOutputY")

# Create the physical event Y > 4
threshold = 4
myEvent = Event(output, Greater(), threshold)

# BEGIN_TEX
# Create the associated standard event in the standard space
myStandardEvent = StandardEvent(myEvent)

# Realization of 'myStandardEvent' as a Bernoulli
print("myStandardEvent realization=", myStandardEvent.getRealization())

# Sample of 10 realizations of 'myStandardEvent  as a Bernoulli
print("myStandardEvent sample=", myStandardEvent.getSample(10))

# END_TEX
