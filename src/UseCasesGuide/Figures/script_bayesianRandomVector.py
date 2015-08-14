#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View


########################
# Case 1
meanDist = Uniform(0,1)
sigmaDist = Exponential(4)

thetaDist = ComposedDistribution(DistributionCollection([meanDist,sigmaDist]))
thetaRV = RandomVector(thetaDist)
Y2 = ConditionalRandomVector(Normal(),thetaRV)

meanMu = meanDist.getMean()[0]
meanSigma = sigmaDist.getMean()[0]

Y1=Normal(meanMu, meanSigma)

n=1000000
sampleY2 = Y2.getSample(n)

# Y2 : Normal kernel smoothing
distRNY2 = KernelSmoothing(Normal(), True, 1024).build(sampleY2)
graph_Y2 = distRNY2.drawPDF()
graph_Y2_draw = graph_Y2.getDrawable(0)
graph_Y2_draw.setLegendName('bayesian random vector')


# Y1 : pdf
graph_distY1 = Y1.drawPDF(-1, 2)
graph_distY1.setTitle('Distribution Y')
graph_distY1.setXTitle('Y')
graph_distY1.setYTitle('PDF')
graph_distY1_draw = graph_distY1.getDrawable(0)
graph_distY1_draw.setLegendName('fixed parameters')
graph_distY1_draw.setColor('blue')
graph_distY1.setDrawable(graph_distY1_draw,0)

# Incorporate the Y2 pdf into the Y1 graph
graph_distY1.add(graph_Y2_draw)

#View(graph_distY1).show()
graph_distY1.draw("pdf_bayesianRandomVector")

# Proba(Y2 > seuil)
seuil = 1.5

funcId = NumericalMathFunction('x', 'x')
Y2RV = RandomVector(funcId,RandomVector(Y2))
evnt = Event( Y2RV, Greater(), seuil)
algoMC = MonteCarlo(evnt)
algoMC.run()
resMC = algoMC.getResult()
print 'proba Y2 = ', resMC.getProbabilityEstimate()

#View(algoMC.drawProbabilityConvergence()).show()

# Proba(Y1 > seuil)
print 'proba Y1 = ', Y1.computeCDF(seuil, True)
