from openturns import *

# Create the conditioned distribution
conditionedDist = Uniform()

# Create the conditioning distribution
conditioningDist = Uniform(-1.0, 1.0)

# Create the ling function g
g = NumericalMathFunction(['y'], ['y', '1+y^2'])

# Create the resulting conditional distribution
finalDist = ConditionalDistribution(conditionedDist, conditioningDist, g)

# Create the pdf graph
graph=finalDist.drawPDF()
graph.setTitle('Conditional distribution')
graph.setXTitle('X')
graph.setYTitle('PDF')
graph_draw = graph.getDrawable(0)
graph_draw.setLegend('')
graph.setDrawable(graph_draw,0)
#Show(graph)
graph.draw('pdf_conditionalDist', 600, 620, GraphImplementation.PDF)

