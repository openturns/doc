from __future__ import print_function
from openturns import *
from math import *

# Generate a scalar sample sampleY
N = 1000
Xsample = Triangular(1.0, 5.0, 10.0).getSample(N)
Ysample = NumericalSample(N, 1)
for i in range(N):
    value = 0.5 + 3 * Xsample[i][0] + Normal().getRealization()[0]
    Ysample[i] = NumericalPoint([value])

# Generate a particular scalar sampleX
particularXSample = Triangular(1.0, 5.0, 10.0).getSample(N)

# BEGIN_TEX
###############################
# Create the linear model from both sample :
# Ysample function of Xsample
###############################
# CARE : Xsample is of dimension n and Ysample of dimension 1
# The level confidence to evaluate the confidence interval is set to 0.90
linearRegressionModel = LinearModelFactory().build(Xsample, Ysample, 0.9)

# Get the coefficients ai
print("coefficients of the linear regression model = ",
      linearRegressionModel.getRegression())

# Get the confidence intervals of the ai coefficients
print("confidence intervals of the coefficients = ",
      linearRegressionModel.getConfidenceIntervals())

# Get the p values of the (n+1) coefficients ai:
print("p-value of each coefficient = ", linearRegressionModel.getPValues())

# Get the residuals
print("residuals values = ",
      linearRegressionModel.getResidual(Xsample, Ysample))

# Evaluate the predictions on the sample particularXSample
print("predicted values on particularXSample = ",
      linearRegressionModel.getPredicted(particularXSample))


###################################################
# GRAPH 1 : Validate the model with a visual test
###################################################
# superposition of clouds (Xsample, Ysample)
# ONLY if Xsample is a SCALAR numerical sample
# + linear regression model

linearRegressionGraph = VisualTest.DrawLinearModel(
    Xsample, Ysample, linearRegressionModel)

# To vizualize the graph
# View(linearRegressionGraph).show()

###################################################
# GRAPH 2 : Draw the graph of the residual values
###################################################
# couples (residual i, residual i+1)
# ONLY if Xsample is a SCALAR numerical sample

residualValuesGraph = VisualTest.DrawLinearModelResidual(
    Xsample, Ysample, linearRegressionModel)

# To vizualize the graph
# View(residualValuesGraph).show()

#############################
# LinearModelRSquared Test tests
# the quality of the linear regression model.
#############################
# It evaluates the R^2 indicator (regression variance analysis)
# and compares it to a level
# H0 = R^2 > level
# Test = True <=> R^2 > level
# p-value threshold : level CARE : it is NOT a probability here!
# p-value : R^2 CARE : it is NOT a probability here!
# Test = True <=> p-value > p-value threshold

# The two following tests must be equal :
# Test 1 : We don't give the linear model which is evaluated and then tested
resultLinearModelRSquared1 = LinearModelTest.LinearModelRSquared(
    Xsample, Ysample, 0.90)

# Test 2 : We give the regression linear model evaluated previously
resultLinearModelRSquared2 = LinearModelTest.LinearModelRSquared(
    Xsample, Ysample, linearRegressionModel, 0.90)

# Print result of the LinearModelRSquared Test
print("Test Succes ? ", (
    resultLinearModelRSquared1.getBinaryQualityMeasure() == 1))

# Get the p-value of the LinearModelRSquared Test
# CARE : it is NOT a probability here! but the R^2 value
print("p-value of the LinearModelRSquared Test = ",
      resultLinearModelRSquared1.getPValue())

# Get the p-value threshold of the LinearModelRSquared Test
# CARE : it is NOT a probability here! but the level=0.90 here
print("p-value threshold = ", resultLinearModelRSquared1.getThreshold())


#############################
#  LinearModelAdjustedRSquared Test tests
# the quality of the linear regression model.
#############################
# It evaluates the adjusted R^2 indicator (regression variance analysis)
# and compare it to a level
# H0 = adjusted aR^2 > level

# The two tests must be equal
# We don't give the linear model which is evaluated and then tested
resultLinearModelAdjustedRSquared1 = LinearModelTest.LinearModelAdjustedRSquared(
    Xsample, Ysample, 0.90)

# We give the regression linear model evaluated previously
resultLinearModelAdjustedRSquared2 = LinearModelTest.LinearModelAdjustedRSquared(
    Xsample, Ysample, linearRegressionModel, 0.90)


#############################
#  LinearModelFisher Test tests
# the nullity of the regression linear model coefficients
# (Fisher distribution used).
#############################
# H0 = the linear relation coefficients are those evaluated by the linear
# regresion

# The two tests must be equal
# Test 1 : We don't give the linear model which is evaluated and then tested
resultLinearModelFisher1 = LinearModelTest.LinearModelFisher(
    Xsample, Ysample, 0.90)

# Test 2 : We give the regression linear model evaluated previously
resultLinearModelFisher2 = LinearModelTest.LinearModelFisher(
    Xsample, Ysample, linearRegressionModel, 0.90)

#############################
#  LinearModelResidualMean Test tests,
# under the hypothesis of a  gaussian sample,
# if the mean of the residual is equal to zero.
#############################
# It is based on the Student test (equality of mean for two gaussian samples).
# H0 = the residuals have a mean equal to zero

# The two tests must be equal
# Test 1 : We don't give the linear model which is evaluated and then tested
resultLinearModelResidualMean1 = LinearModelTest.LinearModelResidualMean(
    Xsample, Ysample, 0.90)

# Test 2 : We give the regression linear model evaluated previously
resultLinearModelResidualMean2 = LinearModelTest.LinearModelResidualMean(
    Xsample, Ysample, linearRegressionModel, 0.90)
# END_TEX
