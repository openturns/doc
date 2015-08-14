from __future__ import print_function
from openturns import *

# Create a vectorial function R ^n --> R^p
# for example R^2 --> R^2
myFunction = NumericalMathFunction(
    ['x1', 'x2'], ['y1', 'y2'], ['1+2*x1+x2', '2+x1+2*x2'])

# Create a scalar function R --> R
func1 = NumericalMathFunction(['x'], ['x^2'])

# Create another function R^2 --> R
func2 = NumericalMathFunction(['x', 'y'], ['x*y'])

# Create a vectorial function R ^3 --> R^2
func3 = NumericalMathFunction(
    ['x1', 'x2', 'x3'], ['y1', 'y2'], ['1+2*x1+x2+x3^3', '2+sin(x1+2*x2)-sin(x3) * x3^4'])

# Create a second vectorial function R ^n --> R^p
# for example R^2 --> R^2
g = NumericalMathFunction(['x1', 'x2'], ['y1', 'y2'], ['x1+x2', 'x1^2+2*x2^2'])

# BEGIN_TEX
# Activate the history mechanism
myFunction.enableHistory()

# Evaluate the function at a particular point
# For example the null vector
point = NumericalPoint(myFunction.getInputDimension(), 1)
imagePoint = myFunction(point)

# Get the input history
myInputHistory = myFunction.getHistoryInput()
# Then get the sample which has been stored
storedSample = myInputHistory.getSample()
print('stored sample = ', storedSample)

# Desactivate the history mechanism
myFunction.disableHistory()

# Ask for the dimension of the input and output vectors
print(myFunction.getInputDimension())
print(myFunction.getOutputDimension())

# Evaluate the gradient of the function at a particular point
gradientMatrix = myFunction.gradient(point)

# Evaluate the hessian of the function at a particular point
hessianMatrix = myFunction.hessian(point)

# Change the gradient evaluation method
# Type : non centered finite difference method
incrGrad = NumericalPoint(myFunction.getInputDimension(), 1.e-7)
myGradient = NonCenteredFiniteDifferenceGradient(
    incrGrad, myFunction.getEvaluation())
print("myGradient = ", myGradient)
# Substitute the gradient
myFunction.setGradient(myGradient)

# Change the hessian evaluation method
# type : centered finite difference method with constant step
myStep = NumericalPoint(myFunction.getInputDimension(), 1.e-7)
myHessian = CenteredFiniteDifferenceHessian(myStep, myFunction.getEvaluation())
print("myHessian = ", myHessian)
# Substitute the hessian
myFunction.setHessian(myHessian)

# Get the number of times the function has been evaluated
callsNumber = myFunction.getEvaluationCallsNumber()

# Get the number of times the gradient has been evaluated
callsNumberGrad = myFunction.getGradientCallsNumber()

# Get the number of times the hessian has been evaluated
callsNumberHes = myFunction.getHessianCallsNumber()

# Get the component i
# Care : the numerotation begins at 0
i = 1
component = myFunction.getMarginal(i)

# Compose the two NumericalMathFunction : h=myFunction o g
h = NumericalMathFunction(myFunction, g)

# Get the valid operators in OpenTURNS
print(NumericalMathFunction.GetValidOperators())

# Get the valid functions in OpenTURNS
print(NumericalMathFunction.GetValidFunctions())

# Get the valid constants in OpenTURNS
print(NumericalMathFunction.GetValidConstants())

# Clear the cache from all the values previoulsy stored
myFunction.clearCache()

#######
# Graph
#######

# General Case : function R ^n --> R^p
# for example R^3 --> R^2
# (x,y,z) --> f(x,y,z) = (f_1(x,y,z), f_2(x,y,z))

#################################
# Graph 1 : z -->  f_2(x_0,y_0,z)
# for z in [-1.5, 1.5] and y_0 = 2. and z_0 = 2.5
# Specify the input component that varies
# Care : numerotation begins at 0
inputMarg = 2
# Give its variation intervall
zMin = -1.5
zMax = 1.5
# Give the coordinates of the fixed input components
centralPt = [1.0, 2.0, 2.5]
# Specify the output marginal function
# Care : numerotation begins at 0
outputMarg = 1
# Specify the point number of the final curve
ptNb = 101
# Draw the curve!
myGraph1 = func3.draw(inputMarg, outputMarg, centralPt, zMin, zMax, ptNb)

###################################
# Graph 2 : (x,z) -->  f_1(x,y_0,z)
# for x in [-1.5, 1.5], z in [-2.5, 2.5]
# and y_0 = 2.5
# Specify the input components that varie
# Care : numerotation begins at 0
firstInputMarg = 0
secondInputMarg = 2
# Give their variation intervall
inputMin2 = [-1.5, -2.5]
inputMax2 = [1.5, 2.5]
# Give the coordinates of the fixed input components
centralPt = [0.0, 2., 2.5]
# Specify the output marginal function
# Care : numerotation begins at 0
outputMarg = 1
# Specify the point number of the final curve
ptNb = [101, 101]
# Draw the curve!
myGraph2 = func3.draw(firstInputMarg, secondInputMarg,
                      outputMarg, centralPt, inputMin2, inputMax2, ptNb)

#################################################
# Graph 3 : simplified method for x -->  func1(x)
# for x in [-1.5, 1.5]
# Give the variation intervall
xMin3 = -1.5
xMax3 = 1.5
# Specify the point number of the final curve
ptNb = 101
# Draw the curve!
myGraph3 = func1.draw(xMin3, xMax3, ptNb)

#################################
# Graph 4 : (x,y) -->  func2(x,y)
# for x in [-1.5, 1.5], y in [-2.5, 2.5]
# Give their variation intervall
inputMin4 = [-1.5, -2.5]
inputMax4 = [1.5, 2.5]
# Give the coordinates of the fixed input components
centralPt = [0.0, 2., 2.5]
# Specify the output marginal function
# Care : numerotation begins at 0
outputMarg = 1
# Specify the point number of the final curve
ptNb = [101, 101]
# Draw the curve!
myGraph4 = func2.draw(inputMin4, inputMax4, ptNb)
# END_TEX

myGraph1.setTitle('Second component of func3 wrt z')
myGraph1.draw('NMFgraph1')
myGraph2.setTitle('Iso-curves of the 2nd comp. of func3 wrt (x,z)')
myGraph2.draw('NMFgraph2')
myGraph3.setTitle('func1 graph')
myGraph3.draw('NMFgraph3')
myGraph4.setTitle('Iso-curves of func2')
myGraph4.draw('NMFgraph4')
