#! /usr/bin/env python

from openturns import *

# set the seed of the random generator
RandomGenerator.SetSeed(77);

#create a sample from a normal distribution X
sample1 = Normal(3.0, 1.0).getSample(150);

# create the reference distribution T
distrib = Normal(4.0, 3.0)
sample1.setName("X / Distribution");
distrib.setName("Distribution")

#create the QQ-plot
qqGraph = VisualTest.DrawQQplot(sample1, distrib)

# set titles
qqGraph.setTitle("");
qqGraph.setXTitle("Value of X");
qqGraph.setYTitle("Distribution");

qqGraph.draw("QQplotDistribBad", 640, 480, GraphImplementation.PDF)

# Case 2 : good QQplot
distrib = Normal(3.0, 1.0)
distrib.setName("Distribution")
qqGraph = VisualTest.DrawQQplot(sample1, distrib)
qqGraph.setTitle("");
qqGraph.setXTitle("Value of X");
qqGraph.setYTitle("Distribution");
qqGraph.draw("QQplotDistribOk", 640, 480, GraphImplementation.PDF)
