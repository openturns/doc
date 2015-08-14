from openturns import *

# Create the conditioned distribution
conditionedDist = Uniform()

# Create the conditioning distribution
conditioningDist = Uniform(-1.0, 1.0)

# Create the ling function g
g = NumericalMathFunction(['y'], ['y', '1+y'])

# Create the resulting conditional distribution
finalDist = BayesDistribution(conditionedDist, conditioningDist, g)

# Generate some realizations
sampleY =   finalDist.getSample(1000)

graph = finalDist.drawPDF([600]*2)
graph.setLegendPosition("topleft")
cloud = Cloud(sampleY)
cloud.setPointStyle("star")
graph.add(cloud)
graph.setLegends(["PDF", "sample"])
graph.setColors(["red", "blue"])
graph.setTitle('PDF and sample from a Bayes distribution')
graph.setXTitle('X')
graph.setYTitle('Y')
graph.draw('pdf_bayesianDist', 600, 620, GraphImplementation.PDF)

