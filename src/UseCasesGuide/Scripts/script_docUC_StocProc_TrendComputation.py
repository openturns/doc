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
# this process is stationary
amplitude = [1.0]
scale = [0.2]
myCovModel = ExponentialModel(myMesh.getDimension(), amplitude, scale)
myXProcess = TemporalNormalProcess(myCovModel, myMesh)

# Create a trend function
# fTrend : R^2 --> R
#          (t,s) --> 1+2t+2s
fTrend = NumericalMathFunction(["t", "s"], ["1+2*t+2*s"])
fTemp = TrendTransform(fTrend)

# Add the trend to the initial process
myYProcess = CompositeProcess(fTemp, myXProcess)

# Get a field from myYtProcess
myYField = myYProcess.getRealization()


# BEGIN_TEX
################################
# CASE 1 : we estimate the trend from the field
################################

# Define the regression stategy using the LAR method
myBasisSequenceFactory = LAR()

# Define the fitting algorithm using the
# Corrected Leave One Out or KFold algorithms
myFittingAlgorithm = CorrectedLeaveOneOut()
myFittingAlgorithm_2 = KFold()

# Define the basis function
# For example composed of 3 functions
func1 = NumericalMathFunction(["t", "s"], ["1"])
func2 = NumericalMathFunction(["t", "s"], ["t"])
func3 = NumericalMathFunction(["t", "s"], ["s"])
func4 = NumericalMathFunction(["t", "s"], ["t^2"])
func5 = NumericalMathFunction(["t", "s"], ["s^2"])
myFunctionBasis = NumericalMathFunctionCollection(0)
myFunctionBasis.add(func1)
myFunctionBasis.add(func2)
myFunctionBasis.add(func3)
myFunctionBasis.add(func4)
myFunctionBasis.add(func5)

# Define the trend function factory algorithm
myTrendFactory = TrendFactory(myBasisSequenceFactory, myFittingAlgorithm)

# Check the definition of the created factory
print('regression stategy : ', myTrendFactory.getBasisSequenceFactory())
print('fitting strategy : ', myTrendFactory.getFittingAlgorithm())

# Create the trend transformation  of type TrendTransform
myTrendTransform = myTrendFactory.build(myYField, Basis(myFunctionBasis))

# Check the estimated trend function
print("Trend function = ", myTrendTransform)


################################
# CASE 2 : we impose the trend (or its inverse)
################################

# The function g computes the trend : R^2 -> R
# g :      R^2 --> R
#          (t,s) --> 1+2t+2s
g = NumericalMathFunction(["t", "s"], ["1+2*t+2*s"])
gTemp = TrendTransform(g)

# Get the inverse trend transformation
# from the trend transform already defined
myInverseTrendTransform = myTrendTransform.getInverse()
print('Inverse trend fucntion = ', myInverseTrendTransform)

# Sometimes it is more useful to define
# the opposite trend h : R^2 -> R
# in fact h = -g
h = NumericalMathFunction(["t", "s"], ["-(1+2*t+2*s)"])
myInverseTrendTransform_2 = InverseTrendTransform(h)

################################
# Remove the trend from the field myYField
# myXField = myYField - f(t,s)
myXField2 = myTrendTransform.getInverse()(myYField)
# or from the class InverseTrendTransform
myXField3 = myInverseTrendTransform(myYField)

# Add the trend to the field myXField2
# myYField = f(t,s) + myXField2
myInitialYField = myTrendTransform(myXField2)

# Get the trend function f(t,s)
myEvaluation_f = myTrendTransform.getEvaluation()

# Evaluate the trend function f at a particular vertex
# which is the lower corner of the mesh
myMesh = myYField.getMesh()
vertices = myMesh.getVertices()
vertex = vertices.getMin()
trend_t = myEvaluation_f(vertex)
# END_TEX
