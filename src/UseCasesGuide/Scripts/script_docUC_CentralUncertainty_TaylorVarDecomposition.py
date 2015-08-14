from __future__ import print_function
from openturns import *

# Create the model (x1,x2) --> (y1,y2) = x1^2 + x2^2
model = NumericalMathFunction(["x1", "x2"], ["y1"], ["x1^2+x2^2"])

inputDist = ComposedDistribution(DistributionCollection(
    [Normal(1., 0.5), Normal(1.0, 0.5)]), IndependentCopula(2))
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
output = RandomVector(model, inputVector)
output.setDescription(["MyOutput"])

# BEGIN_TEX
# Create a quadraticCumul algorithm
myQuadraticCumul = QuadraticCumul(output)

# Compute the several elements provided by the quadratic cumul algorithm
# First order mean
print("First order mean=", myQuadraticCumul.getMeanFirstOrder())
# Second order mean
print("Second order mean=", myQuadraticCumul.getMeanSecondOrder())
# Covariance Matrix
print("Covariance=", myQuadraticCumul.getCovariance())
# Importance factors
# CARE : for this calculus only, the output variable of interest must be
# of dimension 1
print("Importance factors=", myQuadraticCumul.getImportanceFactors())

# Graph 1 : Importance Factors graph
importanceFactorsGraph = myQuadraticCumul.drawImportanceFactors()

# In order to see the graph without creating the associated files
# View(importanceFactorsGraph).show()

# Create the .PNG, .EPS and .FIG files
importanceFactorsGraph.draw("ImportanceFactorsDrawingQuadraticCumul")

# Get the  value of the limit state function at the mean point
meanValue = myQuadraticCumul.getValueAtMean()

# Get the gradient value of the limit state function at the mean point
meanGradient = myQuadraticCumul.getGradientAtMean()

# Get the hessian value of the limit state function at the mean point
meanHessian = myQuadraticCumul.getHessianAtMean()
# END_TEX
