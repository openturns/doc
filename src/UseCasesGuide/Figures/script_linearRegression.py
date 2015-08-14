#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View
from math import *

# CASE 1 : everything is good!
N = 1000
sampleX = Triangular(1.0, 5.0, 10.0).getSample(N)
sampleY = NumericalSample(N,1)
for i in range(N) :
    value = 0.5 + 3 * sampleX[i][0] + Normal().getRealization()[0]
    sampleY[i] = NumericalPoint([value])

linearRegressionModel = LinearModelFactory().build(sampleX, sampleY, 0.9)
#print "coefficient = ", linearRegressionModel.getRegression()
#print "IC coef = ", linearRegressionModel.getConfidenceIntervals()
#print "p-value of each coef = ", linearRegressionModel.getPValues()
#print "residuals = ", linearRegressionModel.getResidual(sampleX, sampleY)

# GRAPH 1 : Validate the model with a visual test :
# superposition of clouds (Xsample, Ysample)
# ONLY if Xsample is a SCALAR numerical sample
# + linear regression model

linearRegressionGraph = VisualTest.DrawLinearModel(sampleX, sampleY, linearRegressionModel)
linearRegressionGraph.draw("linearRegression_Graph")
#View(linearRegressionGraph).show()


# GRAPH 2 : Draw the graph of the residual values
# couples (residual i, residual i+1)
# ONLY if Xsample is a SCALAR numerical sample

residualValuesGraph = VisualTest.DrawLinearModelResidual(sampleX, sampleY, linearRegressionModel)
residualValuesGraph.draw("linearRegression_residualGraph")
#View(residualValuesGraph).show()

# Case 2 : everything goes wrong!

sampleY2 = NumericalSample(N,1)
for i in range(N) :
    sampleY2[i] = NumericalPoint(1, sampleX[i][0] *  sampleX[i][0] + Normal(0.0, 1.0).getRealization()[0])

linearRegressionModel2 = LinearModelFactory().build(sampleX, sampleY2, 0.9)
#print "coefficient = ", linearRegressionModel2.getRegression()
#print "IC coef = ", linearRegressionModel2.getConfidenceIntervals()
#print "p-value of each coef = ", linearRegressionModel2.getPValues()
#print "residuals = ", linearRegressionModel2.getResidual(sampleX, sampleY2)

# GRAPH 1 : Validate the model with a visual test :
# superposition of clouds (Xsample, Ysample)
# ONLY if Xsample is a SCALAR numerical sample
# + linear regression model

linearRegressionGraph2 = VisualTest.DrawLinearModel(sampleX, sampleY2, linearRegressionModel2)
linearRegressionGraph2.draw("linearRegression_GraphWrong")
#View(linearRegressionGraph2).show()


# GRAPH 2 : Draw the graph of the residual values
# couples (residual i, residual i+1)
# ONLY if Xsample is a SCALAR numerical sample

residualValuesGraph2 = VisualTest.DrawLinearModelResidual(sampleX, sampleY2, linearRegressionModel2)
residualValuesGraph2.draw("linearRegression_residualGraphWrong")
#View(residualValuesGraph2).show()

# Case 3 : everything goes wrong!

sampleY3 = NumericalSample(N,1)
for i in range(N) :
    sampleY3[i] = NumericalPoint(1, sin(pi*sampleX[i][0]) + Normal(0.0, 0.1).getRealization()[0])

linearRegressionModel3 = LinearModelFactory().build(sampleX, sampleY3, 0.9)
#print "coefficient = ", linearRegressionModel3.getRegression()
#print "IC coef = ", linearRegressionModel3.getConfidenceIntervals()
#print "p-value of each coef = ", linearRegressionModel3.getPValues()
#print "residuals = ", linearRegressionModel3.getResidual(sampleX, sampleY3)

# GRAPH 1 : Validate the model with a visual test :
# superposition of clouds (Xsample, Ysample)
# ONLY if Xsample is a SCALAR numerical sample
# + linear regression model

linearRegressionGraph3 = VisualTest.DrawLinearModel(sampleX, sampleY3, linearRegressionModel3)
linearRegressionGraph3.draw("linearRegression_GraphWrong2")
#View(linearRegressionGraph3).show()


# GRAPH 2 : Draw the graph of the residual values
# couples (residual i, residual i+1)
# ONLY if Xsample is a SCALAR numerical sample

residualValuesGraph3 = VisualTest.DrawLinearModelResidual(sampleX, sampleY3, linearRegressionModel3)
residualValuesGraph3.draw("linearRegression_residualGraphWrong2")
#View(residualValuesGraph3).show()
