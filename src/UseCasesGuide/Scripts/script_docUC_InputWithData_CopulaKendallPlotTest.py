from __future__ import print_function
from openturns import *

# Create a bidimensionnal sample
# For example :
dist = ComposedDistribution([Normal(), Normal()], GumbelCopula(3))
N = 500
sample1 = dist.getSample(N)
sample1.setName('sample1')

# Create another distribution and sample
dist2 = ComposedDistribution([Normal(), Normal()], ClaytonCopula(0.2))
N = 500
sample2 = dist2.getSample(N)
sample2.setName('sample2')

# BEGIN_TEX
##################################
# CASE 1 : Test a specific copula model for a given sample
##################################

# Change the parameter for the evaluation of E(Wi)
myValue = 25
ResourceMap.SetAsUnsignedInteger(
    'VisualTest-KendallPlot-MonteCarloSize', myValue)

# Run the Kendall test
# For example on the Gumbel Copula(3)
copula_test = GumbelCopula(3)
kendallPlot1 = VisualTest.DrawKendallPlot(sample1, copula_test)

# Visualize the graph
# View(kendallPlot1).show()


##################################
# CASE 2 : Test whether two samples have the same copula model
##################################

# Run the Kendall test
kendallPlot2 = VisualTest.DrawKendallPlot(sample1, sample2)

# Visualize the graph
# View(kendallPlot2).show()

# Print the graph in file.PNG
kendallPlot2.draw('copula_validation', 640, 480, GraphImplementation.PNG)
# END_TEX
