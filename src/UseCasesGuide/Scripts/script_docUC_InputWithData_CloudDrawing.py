from __future__ import print_function
from openturns import *

# Create a bidimensionnal sample
# For example fomr a Normal distribution
mean2d = NumericalPoint(2)
sigma2d = NumericalPoint([2., 1.5])
corrMat2d = CorrelationMatrix(2)
corrMat2d[0, 1] = 0.8
dist2d = Normal(mean2d, sigma2d, corrMat2d)
N = 500
sample2d = dist2d.getSample(N)

# For example, for a 4d Normal distribution
# with correlation matrix
mean4d = NumericalPoint(4)
sigma4d = NumericalPoint([2.0, 1.5, 1.0, 0.5])
corrMat4d = CorrelationMatrix(4)
corrMat4d[0, 1] = 0.8
corrMat4d[0, 2] = 0.0
corrMat4d[0, 3] = 0.0
corrMat4d[1, 2] = 0.0
corrMat4d[1, 3] = 0.0
corrMat4d[2, 3] = -0.7
dist4d = Normal(mean4d, sigma4d, corrMat4d)
N = 500
sample4d = dist4d.getSample(N)


# BEGIN_TEX
###################################
# Create a 2d cloud

# Create the cloud Drawable
# cloud : filled squares in blue
myCloud = Cloud(sample2d, "blue", "fsquare", "First Cloud")

# Then, insert it into a Graph structure
myGraph2d = Graph("My Sample 2d", "x1", "x2", True, "topright")
myGraph2d.add(myCloud)


###################################
# Create all the pairs of 2d clouds

myPairs = Pairs(sample4d, 'My Pairs', Description(
    ['Var1', 'Var2', 'Var3', 'Var4']), 'red', 'circle')

# Then, insert it into a Graph structure
myGraph4d = Graph()
myGraph4d.add(myPairs)
# END_TEX

# Use Cases Guide graph
myGraph4d.draw('pairs', 800, 600, GraphImplementation.PDF)
myGraph4d.draw('pairs', 800, 600, GraphImplementation.PNG)
