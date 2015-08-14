#! /usr/bin/env python

from openturns import *
#create a sample from a normal distributon
sample = Normal(10.0, 2.0).getSample(50)
sample.setName("X")

#compute henry line
henryGraph = VisualTest().DrawHenryLine(sample);

#drawing the final graph in to file (henryGraph.eps and henryGraph.png)
diagonal = henryGraph.getDrawable(0)
diagonal.setLegendName("T=(X-10)/2")
henryGraph.setXTitle("Value of X")
henryGraph.setYTitle("Value of T")
henryGraph.draw("henryGraph", 640, 480, DrawableImplementation.PNG)
