#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View


normal = Normal(0.0,1.0)
sample = normal.getSample(1000)
data_hist = VisualTest.DrawHistogram(sample)
data_hist.draw("hist_Data")
#View(data_hist).show()
