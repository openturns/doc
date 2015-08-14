#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View

normal = Normal(0.0, 1.0)
sample = normal.getSample(1000)

sampleHenryLine = VisualTest.DrawHenryLine(sample)
sampleHenryLine.draw("HenryLineTestRight")
#View(sampleHenryLine).show()

sample2 = Beta(0.7, 1.6, 0.0, 2.0).getSample(1000)
sample2HenryLine = VisualTest.DrawHenryLine(sample2)
sample2HenryLine.draw("HenryLineTestFalse")
#View(sample2HenryLine).show()
