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

# Create the associated standard event in the standard space
myStandardEvent = StandardEvent(myEvent)

###################
# First : FORM analyses to get the design point
###################
myCobyla = Cobyla()
myStartingPoint = inputDist.getMean()
myAlgoFORM = FORM(myCobyla, myEvent, myStartingPoint)
myAlgoFORM.run()
FORMResult = myAlgoFORM.getResult()
standardSpaceDesignPoint = FORMResult.getStandardSpaceDesignPoint()

#############################
# Second : Strong Max Test
#############################

# BEGIN_TEX
# Fix the importance level epsilon of the test
# Care : 0<epsilon<1
importanceLevel = 0.15

# Fix the accuracy level tau of the test
# Care : tau >0
# It is recommended that tau <4
accuracyLevel = 3

# Fix the confidence level (1-q) of the test
confidenceLevel = 0.99

# Create the Strong Maximum Test
# CARE : the event must be declared in the standard space
# 1. From the confidenceLevel parameter
mySMT_CL = StrongMaximumTest(
    myStandardEvent, standardSpaceDesignPoint,  importanceLevel, accuracyLevel,  confidenceLevel)

# 2. Or from the  maximum number of points sampling the sphere
pointsNumber = 1000
mySMT_PN = StrongMaximumTest(
    myStandardEvent, standardSpaceDesignPoint,  importanceLevel, accuracyLevel,  pointsNumber)

# Perform the test
mySMT_CL.run()
mySMT_PN.run()

# Get (or evaluate) the confidence level
# associated to the number of points used to sample the sphere
print('Confidence level = ', mySMT_CL.getConfidenceLevel())

# Get (or evaluate) the number of points used to sample the sphere
# associated the confidence level used
print('Points Number = ', mySMT_CL.getPointNumber())

# Get all the points verifying the event  and outside the design point vicinity
# Get also the values of limit state function at these points
potentialDesignPoints = mySMT_CL.getFarDesignPointVerifyingEventPoints()
values = mySMT_CL.getFarDesignPointVerifyingEventValues()
print('Potential design points = ', end=' ')
print(potentialDesignPoints)
print('Model values = ')
print(values)

# Get all the points verifying the event and inside the design point vicinity
# Get also the values of limit state function at these points
vicinityDesignPoint = mySMT_CL.getNearDesignPointVerifyingEventPoints()
values = mySMT_CL.getNearDesignPointVerifyingEventValues()
print(
    'Points verifying the Event in the vicinity of the design points = ', end=' ')
print(vicinityDesignPoint)
print('Model values = ')
print(values)

# Get all the points not verifying the event and outside the design point vicinity
# Get also the values of limit state function at these points
farSecurityPoints = mySMT_CL.getFarDesignPointViolatingEventPoints()
values = mySMT_CL.getFarDesignPointViolatingEventValues()
print(
    'Points NOT verifying the Event outside the vicinity of the design points = ', end=' ')
print(farSecurityPoints)
print('Model values = ')
print(values)

# Get  all the points not verifying the event and inside the design point vicinity
# Get also the values of limit state function at these points
vicinitySecurityPoints = mySMT_CL.getNearDesignPointViolatingEventPoints()
values = mySMT_CL.getNearDesignPointViolatingEventValues()
print(
    'Points NOT verifying the Event outside the vicinity of the design points = ', end=' ')
print(vicinitySecurityPoints)
print('Model values = ')
print(values)
# END_TEX
