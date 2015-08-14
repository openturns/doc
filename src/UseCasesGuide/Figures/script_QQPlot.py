#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View

beta = Beta(1.2,3.4,1.0, 2.0)
sample = beta.getSample(1000)

betaPDF = beta.drawPDF()
betaPDF.draw("BetaPDFajeter")
#View(betaPDF).show()

sampleQQplot = VisualTest.DrawQQplot(sample,Distribution(beta),100)
sampleQQplot.draw("beta_QQplot")
#View(sampleQQplot).show()

weibull = Weibull(1.5, 1.0, 1.0)
sampleFalseQQplot = VisualTest.DrawQQplot(sample,Distribution(weibull),100)
sampleFalseQQplot.draw("weibull_QQplot")
#View(sampleFalseQQplot).show()
