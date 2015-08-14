from __future__ import print_function
from openturns import *

# Case 1 : the distribution of theta is explicitely known
# The distribution of Theta : dimension 2
myThetaDist = ComposedDistribution(
    [Normal(), Exponential(0.2)], IndependentCopula(2))

# Case 2 : the random vector Theta is the result of f(Y)
# Create the model Theta = (y1 + 2*y2)
model = NumericalMathFunction(["y1", "y2"], ["theta"], ["y1+2*y2"])
# Create the input distribution and random vector Y
inputDistY = ComposedDistribution(
    DistributionCollection([Normal(), Normal()]), IndependentCopula(2))
inputDistY.setDescription(['Y1', 'Y2'])
# create the Y random vector
inputYRV = RandomVector(inputDistY)

# Create the X given Theta distribution : Normal
myX_ThetaDist = Normal()

# BEGIN_TEX
# First , create the random vector associated to the theta distribution

# Case 1 : the distribution of theta is explicitely known
# we create the random vector from the distribution
myThetaRV_1 = RandomVector(myThetaDist)

# Case 2 : the random vector Theta is the result of f(X)
# and has been already defined previoulsy in the study
# from a command such as
myThetaRV_2 = RandomVector(model, inputYRV)

# Case 3 : the random vector Theta is any RandomVector
# it can result from : PythonRandomVector, FunctionalChaosRandomVector,
# Event, ...


# Then create the conditional random vector X
XrandomVector = ConditionalRandomVector(myX_ThetaDist, myThetaRV_1)

# Generate some realizations of the conditional random vector X
sampleX = XrandomVector.getSample(10)

# Get the distribution of X given Theta
# with the  parameters used for the last realization
# of XrandomVector
conditionalModel = XrandomVector.getDistribution()

# Get the random vector Theta
rdTheta = XrandomVector.getRandomParameters()

# END_TEX
