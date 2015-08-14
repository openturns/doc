#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *

colors = ["red", "green", "blue", "magenta", "orange"]
# Random Walk 1d et distribution discrete
myOrigin = NumericalPoint([0.0])
tMin = 0.
timeStep = 1
n=500
myTimeGrid = RegularGrid(tMin,timeStep, n)
myDistribution = UserDefined([[-1], [10]],[0.9, 0.1] )


myRandomWalk = RandomWalk(myOrigin, myDistribution, myTimeGrid)
realization = myRandomWalk.getSample(5)
myGraph = realization.drawMarginal(0)
myGraph.setLegendPosition('')
myGraph.setTitle('1D Random Walk with discrete steps')
#View(myGraph).show()
myGraph.draw('randomwalk1D_discrete', 800, 600, GraphImplementation.PDF)
myGraph.draw('randomwalk1D_discrete', 800, 600, GraphImplementation.PNG)


####################################################
# Random Walk 1d et distribution continue
myDistribution = Normal(0,1)

myRandomWalk = RandomWalk(myOrigin, myDistribution, myTimeGrid)
realization = myRandomWalk.getSample(5)
myGraph = realization.drawMarginal(0)
myGraph.setLegendPosition('')
myGraph.setTitle('1D Random Walk with continuous steps')
#View(myGraph).show()
myGraph.draw('randomwalk1D_continuous', 800, 600, GraphImplementation.PDF)
myGraph.draw('randomwalk1D_continuous', 800, 600, GraphImplementation.PNG)



####################################################
# Random Walk 2d et distribution discrete
myOrigin = NumericalPoint([0.0, 0.0])
tMin = 0.
timeStep = 1
n=500
myTimeGrid = RegularGrid(tMin,timeStep, n)
myDistribution = UserDefined([[-1., -2.], [1., 3.]], [0.5, 0.5])
myDistribution.getRealization()


myRandomWalk = RandomWalk(myOrigin, myDistribution, myTimeGrid)
realization = myRandomWalk.getSample(5)
myGraph = Graph('2D Random Walk with discrete steps', 'X1', 'X2', True)
pal=Drawable.GetValidColors()
for i in range(5) :
  values = realization[i].getSample()
  myGraph.add(Curve(values, pal[i], 'solid'))

myGraph.setTitle('2D Random Walk with discrete steps')
#View(myGraph).show()
myGraph.draw('randomwalk2D_discrete', 800, 600, GraphImplementation.PDF)
myGraph.draw('randomwalk2D_discrete', 800, 600, GraphImplementation.PNG)



####################################################
# Random Walk 2d et distribution continue
myOrigin = NumericalPoint([0.0, 0.0])
tMin = 0.
timeStep = 1
n=500
myTimeGrid = RegularGrid(tMin,timeStep, n)

myDistribution = Normal(2)

myRandomWalk = RandomWalk(myOrigin, myDistribution, myTimeGrid)
realization = myRandomWalk.getSample(5)
myGraph = Graph('2D Random Walk with continuous steps', 'X1', 'X2', True)
pal=Drawable.GetValidColors()
for i in range(5) :
  curve = Curve(realization[i].getSample())
  curve.setColor(colors[i])
  myGraph.add(curve)

myGraph.setTitle('2D Random Walk with continuous steps')
#View(myGraph).show()
myGraph.draw('randomwalk2D_continuous', 800, 600, GraphImplementation.PDF)
myGraph.draw('randomwalk2D_continuous', 800, 600, GraphImplementation.PNG)
