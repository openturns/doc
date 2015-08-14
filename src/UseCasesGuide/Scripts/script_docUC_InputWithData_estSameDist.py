from __future__ import print_function
from openturns import *

# Generate two scalar sample
sample1 = Normal().getSample(100)
sample1.setName('sample 1')
sample2 = Normal().getSample(100)
sample2.setName('sample 2')

# BEGIN_TEX
#########################
# GRAPH 1 : QQ-plot graph
#########################

# Generate the Graph structure for the QQ-plot graph
# number of points of the graph fixed to 100 (20 by default)
twoSamplesQQPlot = VisualTest.DrawQQplot(sample1, sample2, 100)

# To visualize the graph
# View(twoSamplesQQPlot).show()

# Draw the graph on the file twoSamplesQQPlot.png and twoSamplesQQPlot.eps
# if the file adress is not fulfilled, the file is created in the current
# directory
twoSamplesQQPlot.draw("twoSamplesQQPlot")

#########################
# Smirnov Test :
# have both samples  a monotonous relation ?
#########################

# H0 : same continuous distribution
# Test = True <=> same continuous distribution
# p-value threshold : probability of the H0 reject zone : 1-0.90
# p-value : probability (test variable decision > test variable decision evaluated on the samples)
# Test = True <=> p-value > p-value threshold
resultSmirnov = HypothesisTest.Smirnov(sample1, sample2, 0.90)
# END_TEX
