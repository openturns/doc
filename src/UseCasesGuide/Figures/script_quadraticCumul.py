#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View

myFunction = NumericalMathFunction("poutre")

distributionE = Beta(0.94,3.19,2.78e7,4.83e7)
distributionF = LogNormal(30000.0, 9000.0, 15000, 1)
distributionL = Uniform(250, 260)
distributionI = Beta(2.5,4.0,3.1e2,4.5e2)

collectionMarginales = DistributionCollection(4)
collectionMarginales[0] = distributionE
collectionMarginales[1] = distributionF
collectionMarginales[2] = distributionL
collectionMarginales[3] = distributionI

# The independent copula is assumed if no copula is given
inputDistribution = ComposedDistribution(collectionMarginales)

inputDesc = Description(4)
inputDesc[0] = "E"
inputDesc[1] = "F"
inputDesc[2] = "L"
inputDesc[3] = "I"
inputDistribution.setDescription(inputDesc)


input = RandomVector(inputDistribution)
descrip = Description(4)
descrip[0]  ="E"
descrip[1]  ="F"
descrip[2]  ="L"
descrip[3]  ="I"
input.setDescription(descrip)

output =  RandomVector(myFunction, input)

myQuadraticCumul = QuadraticCumul(output)
meanFO = myQuadraticCumul.getMeanFirstOrder()
meanSO = myQuadraticCumul.getMeanSecondOrder()
IF = myQuadraticCumul.getImportanceFactors()
importanceFactorsGraph = myQuadraticCumul.drawImportanceFactors()
importanceFactorsGraph.draw("ImportanceFactorsDrawingQuadraticCumul")
#View(importanceFactorsGraph).show()
