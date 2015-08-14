from __future__ import print_function
from openturns import *

# Create here the python lines to define the implementation of the function

# In order to be able to use that function with the openturns library,
# it is necessary to define a class which derives from OpenTURNSPythonFunction


class modelePYTHON(OpenTURNSPythonFunction):
    # that following method defines the input size (4) and the output size (1)

    def __init__(self):
        OpenTURNSPythonFunction.__init__(self, 4, 1)

    # that following method gives the implementation of modelePYTHON
    def _exec(self, x):
        E = x[0]
        F = x[1]
        L = x[2]
        I = x[3]
        return [-(F * L * L * L) / (3. * E * I)]

# Use that function defined in the script python
# with the openturns library
# Create a NumericalMathFunction from modelePYTHON
poutre = NumericalMathFunction(modelePYTHON())

# BEGIN_TEX
# Dimension of the random input vector
stochasticDimension = 2

# Dimension of the deterministic input vector
deterministicDimension = 2

# Dimension of the input vector of the limit state function 'poutre'
inputDim = poutre.getInputDimension()

# Fixe deterministic values for the two last variables
# of the input vecteor (E,F,L,I)
# L
X2 = 10.0
# I
X3 = 5.0

# Create the analyticalfunction 'increase'
increase = NumericalMathFunction(
    ["E", "F"], ["E", "F", "L", "I"], ["E", "F", str(X2), str(X3)])

# Create the new limit state function :
# 'poutreReduced = poutre o increase'
poutreReduced = NumericalMathFunction(poutre, increase)

# Give directly to the 'poutreReduced' function a gradient evaluation method
# thanks to the finite difference technique
# For example, gradient technique : non centered finite difference method
myGradient = NonCenteredFiniteDifferenceGradient(
    NumericalPoint(2, 1.0e-7), poutreReduced.getEvaluation())
print("myGradient = ", myGradient)

# Substitute the gradient
poutreReduced.setGradient(myGradient)

# Give directly to the 'poutreReduced' function a hessian evaluation method
# thanks to the finite difference technique
# type : non centered finite difference method
myHessian = CenteredFiniteDifferenceHessian(
    NumericalPoint(2, 1.0e-7), poutreReduced.getEvaluation())
print("myHessian = ", myHessian)

# Substitute the hessian
poutreReduced.setHessian(myHessian)
# END_TEX
