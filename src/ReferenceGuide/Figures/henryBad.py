#! /usr/bin/env python

from openturns import *

sample = LogNormal(2.0, 1.0, 0.0).getSample(50)
sample.setName("X")

#Compute henry line
henryGraph = VisualTest.DrawHenryLine(sample);

# Draw the graph
henryGraph.setXTitle("Value of X")
henryGraph.setYTitle("Value of T")
henryGraph.draw("henryBadGraph", 640, 480, GraphImplementation.PDF)
