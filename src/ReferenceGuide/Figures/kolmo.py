#! /usr/bin/env python

from openturns import *
#create the sample {5,6,10,22,27}
sample = NumericalSample(0, 1)
sample.add(NumericalPoint(1, 5.0))
sample.add(NumericalPoint(1, 6.0))
sample.add(NumericalPoint(1, 10.0))
sample.add(NumericalPoint(1, 22.0))
sample.add(NumericalPoint(1, 27.0))
sample.setName("Empirical")

#compute the empirical cumulative density function from the sample
graph = VisualTest.DrawEmpiricalCDF(sample, 0, 30);

# get the cdf drawable (it is the only way to mix two (or more) graphics)
empiricalDrawable = graph.getDrawables()[0];
# modify the cdf graphics color
empiricalDrawable.setColor("darkblue");

#create the candidate distribution (exponantial)
candidate = Exponential(0.07, 0.0);
candidate.setName("Candidate");
# compute candidate CDF ( x-coordinate in [0,30])
graph = candidate.drawCDF(0.0, 30.0);
# add empirical cdf to the graph
graph.add(empiricalDrawable);
# create image files
graph.draw("kolmo", 640, 480, GraphImplementation.PDF);
