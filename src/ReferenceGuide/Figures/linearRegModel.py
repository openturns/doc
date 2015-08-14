#! /usr/bin/env python
from openturns import *
from math import *

N = 1000
#create a sample X
dist = Triangular(1.0, 5.0, 10.0)
# create a Y sample : Y = 0.5 + 3 * X + eps
eps = Normal(0.0, 1.0)
sample = ComposedDistribution(DistributionCollection([dist, eps])).getSample(N)
sampleY = NumericalMathFunction(Description(["x", "eps"]), Description(["y"]), Description(["0.5+3.0*x+eps"]))(sample)
sampleY.setName("Ysample")
sampleX = sample.getMarginal(0)
sampleX.setName("Xsample")
#create a linear model
linearModelFact = LinearModelFactory()
#fit this linear model
regressionModel = linearModelFact.build(sampleX, sampleY, 0.9)

# Test the linear model fitting
lmGraph = VisualTest.DrawLinearModel(sampleX, sampleY, regressionModel)

lmDrawables = lmGraph.getDrawables()
lmDrawables[1].setPointStyle("times")
lmGraph.setDrawables(lmDrawables)
lmGraph.setXTitle("X1")
lmGraph.setYTitle("X2")
lmGraph.setTitle("")
# copy the graph in a file
lmGraph.draw("OKlinearRegModel", 640, 380, GraphImplementation.PDF)

lmGraph = VisualTest.DrawLinearModelResidual(sampleX, sampleY, regressionModel)

lmDrawables = lmGraph.getDrawables()
lmDrawables[0].setPointStyle("times")
lmGraph.setDrawables(lmDrawables)
lmGraph.setXTitle("X1")
lmGraph.setYTitle("X2")
lmGraph.setTitle("")
# copy the graph in a file
lmGraph.draw("OKlinearRegModelResidual", 640, 380, GraphImplementation.PDF)


#second grpah : wrong :

#Y2 = exp(X/2) + eps
sampleY2 = NumericalMathFunction(Description(["x", "eps"]), Description(["y"]), Description(["exp(0.5*x)+eps"]))(sample)

# same as good test
regressionModel2 = LinearModelFactory().build(sampleX, sampleY2, 0.9)
lmGraph = VisualTest.DrawLinearModel(sampleX, sampleY2, regressionModel2)
lmDrawables = lmGraph.getDrawables()
lmDrawables[1].setPointStyle("times")
lmGraph.setDrawables(lmDrawables)
lmGraph.setXTitle("X1")
lmGraph.setYTitle("X2")
lmGraph.setTitle("")
lmGraph.draw("WronglinearRegModel", 640, 380, GraphImplementation.PDF)

lmGraph = VisualTest.DrawLinearModelResidual(sampleX, sampleY2, regressionModel2)
lmDrawables = lmGraph.getDrawables()
lmDrawables[0].setPointStyle("times")
lmGraph.setDrawables(lmDrawables)
lmGraph.setXTitle("X1")
lmGraph.setYTitle("X2")
lmGraph.setTitle("")
lmGraph.draw("WronglinearRegModelResidual", 640, 380, GraphImplementation.PDF)
