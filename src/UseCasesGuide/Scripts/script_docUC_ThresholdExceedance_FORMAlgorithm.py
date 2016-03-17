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

# Create the event Y > 4
threshold = 4
myEvent = Event(output, Greater(), threshold)

# BEGIN_TEX
# Create a NearestPoint algorithm with the Cobyla algorithm
myCobyla = Cobyla()

# It is possible to change the default values of the specific parameters :
myValue = 0.2
myCobyla.setRhoBeg(myValue)

# Change the general parameters of the algorithm
myCobyla.setMaximumIterationNumber(100)
myCobyla.setMaximumAbsoluteError(1.0e-6)
myCobyla.setMaximumRelativeError(1.0e-6)
myCobyla.setMaximumResidualError(1.0e-6)
myCobyla.setMaximumConstraintError(1.0e-6)
print("myCobyla=", myCobyla)

# Create a NearestPoint algorithm
# with the AbdoRackwitz algorithm
myAbdoRackwitz = AbdoRackwitz()
# or with the SQP algorithm
mySQP = SQP()

# Create a FORM or SORM algorithm :
# The first parameter is a NearestPointAlgorithm
# The second parameter is an Event in the physical space
# The third parameter is a starting point for the design point research

# The starting point is fixed to the mean of the input distributino
myStartingPoint = inputDist.getMean()

myAlgoFORM = FORM(myCobyla, myEvent, myStartingPoint)
print("FORM=", myAlgoFORM)

myAlgoSORM = SORM(myCobyla, myEvent, myStartingPoint)
print("SORM=", myAlgoSORM)
# END_TEX
