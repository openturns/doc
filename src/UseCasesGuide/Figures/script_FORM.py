#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View

myFunction = NumericalMathFunction("poutre")

distributionE = Beta(0.94,3.19,2.78e7,4.83e7)
distributionF = LogNormal(30000.0, 9000.0, 15000, 1)
distributionL = Uniform(250, 260)
distributionI = Beta(2.5,4.0,3.1e2,4.5e2)

inputDistribution = ComposedDistribution([distributionE, distributionF, distributionL,distributionI ])
inputDistribution.setDescription(["E","F", "L", "I" ])


input = RandomVector(inputDistribution)
input.setDescription(["E","F", "L", "I" ])

output =  RandomVector(myFunction, input)




myAlgoOptim = SQP()
myAlgoOptim.setSpecificParameters(AbdoRackwitzSpecificParameters())
myAlgoOptim.setMaximumIterationsNumber(1000)
myAlgoOptim.setMaximumAbsoluteError(1.0e-10)
myAlgoOptim.setMaximumRelativeError(1.0e-10)
myAlgoOptim.setMaximumResidualError(1.0e-10)
myAlgoOptim.setMaximumConstraintError(1.0e-10)

myEvent = Event(output,Less(), -30, "Event 1")

mean = input.getMean()
myAlgo = FORM(myAlgoOptim, myEvent, mean)
myAlgo.run()
result = myAlgo.getResult()

####################################
# Graph 1: Error history
# Check the convergence criteria of the algorithm
optimResult = result.getOptimizationResult()
# In particular, draw the error histories
graphErrors = optimResult.drawErrorHistory()
graphErrors.setLegendPosition('bottomleft')
graphErrors.draw('ErrorHistoryFORM', 800, 600, GraphImplementation.PNG)
Show(graphErrors)



####################################
# Graph 2 : Importance Factors graph
importanceFactorsGraph = result.drawImportanceFactors()
importanceFactorsGraph.draw("ImportanceFactorsDrawingFORM")

# View the bitmap file
#View(importanceFactorsGraph).show()


####################################
# Graph 3 : Hasofer Reliability Index Sensitivity Graphs graph
reliabilityIndexSensitivityGraphs = result.drawHasoferReliabilityIndexSensitivity()

# Sensitivity to parameters of the marginals of
# the input probabilistic vector
graph2a = reliabilityIndexSensitivityGraphs[0]
graph2a.setLegendPosition("bottomright")
graph2a.draw("HasoferReliabilityIndexMarginalSensitivityDrawing")

# View the bitmap file
#View(graph2a).show()

####################################
# Graph 4 : FORM Event Probability Sensitivity Graphs graph
eventProbabilitySensitivityGraphs = result.drawEventProbabilitySensitivity()

# Sensitivity to parameters of the marginals of the input probabilistic vector
graph3a = eventProbabilitySensitivityGraphs[0]
graph3a.draw("EventProbabilityIndexMarginalSensitivityDrawing")

# View the bitmap file
#View(graph3a).show()


####################################
