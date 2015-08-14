#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View


c=Normal(NumericalPoint(2,2.0), NumericalPoint(2,1.0), CorrelationMatrix(2))
R = CorrelationMatrix(2)
R[0,1] = -0.8
c=Normal(NumericalPoint(2,2.0), NumericalPoint(2,1.0), CorrelationMatrix(2))
R[0,1] = 0.8
c2=Normal(NumericalPoint(2,2.0), NumericalPoint(2,1.0), R)
sample = c.getSample(10000)
cloud1 = VisualTest.DrawClouds(sample,Distribution(c2))

cloud1.draw("cloud1")
#View(cloud1).show()
