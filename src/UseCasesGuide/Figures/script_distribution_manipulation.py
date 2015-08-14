from openturns import *
from openturns.viewer import View
from math import *

n = 10
R = 6.0

# Graph Tulipe1
coll = DistributionCollection(n + 1)
for i in range(n):
  theta = 2.0 * pi * i / float(n)
  mean = NumericalPoint(2)
  mean[0] = R * cos(theta)
  mean[1] = R * sin(theta)
  dist = Normal(2)
  dist.setMean(mean)
  coll[i] = dist

coll[n] = Normal(NumericalPoint(2, 0.0), NumericalPoint(2, 1.2), CorrelationMatrix(2))

distribution = Mixture(coll)

xMin = [-10.0, -10.0]
xMax = [10.0, 10.0]
pointNumber = [101, 101]
graph1=distribution.drawPDF(xMin, xMax, pointNumber)
graph1.setTitle("Iso-PDF - Example1")
graph1.draw("contour2D_tulipe", 800, 600, GraphImplementation.PNG)
graph1.draw("contour2D_tulipe", 800, 600, GraphImplementation.PDF)
#View(graph1).show()

# Graph Tulipe2
coll = DistributionCollection(2)

collMarginal = DistributionCollection(3)
collMarginal[0] = Normal(-5,1)
collMarginal[1] = Normal(0,2)
collMarginal[2] = Normal(6,1)
dist = Mixture(collMarginal)
dist.setName("Marginal 1 :  mixture of normals")

coll[0] = dist

collMarginal[0] = Normal(-5,1)
collMarginal[1] = Normal(0,1.2)
collMarginal[2] = Normal(5,1.5)
dist = Mixture(collMarginal)
dist.setName("Marginal 2 :  mixture of normals")

coll[1] = dist

copula = GumbelCopula(3.5)
#copula = IndependentCopula(2)
distribution = ComposedDistribution(coll, copula)

xMin = [-10.0, -10.0]
xMax = [10.0, 10.0]
pointNumber = [201, 201]
graph2=distribution.drawPDF(xMin, xMax, pointNumber)
graph2.setTitle("Iso-PDF - Example2")
graph2.draw("contour2D_2", 800, 600, GraphImplementation.PNG)
graph2.draw("contour2D_2", 800, 600, GraphImplementation.PDF)
#View(graph2).show()
