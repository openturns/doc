#! /usr/bin/env python

from openturns import *

RandomGenerator.SetSeed(100)

#Case 1: Bad QQplot
#create two samples from two different Normal distribution
sample1 = Normal(3.0, 3.0).getSample(150)
sample2 = Normal(2.0, 1.0).getSample(150)

#create qqplot
qqGraph = VisualTest.DrawQQplot(sample1, sample2)
drawable = qqGraph.getDrawable(1)
drawable.setLegendName("X / X prime")
qqGraph.setDrawable(drawable, 1)
qqGraph.setTitle("")
qqGraph.setXTitle("Quantile of X")
qqGraph.setYTitle("Quantile of X prime")

# create graphics file
qqGraph.draw("QQplotBad", 640, 480, GraphImplementation.PDF)

#Case 2 : Good QQplot
#create two samples from the same distribution
sample3 = Normal(3.0, 2.0).getSample(150)
sample4 = Normal(3.0, 2.0).getSample(150)
#same as case 1
qqGraph = VisualTest.DrawQQplot(sample3, sample4)
drawable = qqGraph.getDrawable(1)
drawable.setLegendName("X / X prime")
qqGraph.setDrawable(drawable, 1)
qqGraph.setTitle("")
qqGraph.setXTitle("Quantile of X")
qqGraph.setYTitle("Quantile of X prime")

qqGraph.draw("QQplotOk", 640, 480, GraphImplementation.PDF)
