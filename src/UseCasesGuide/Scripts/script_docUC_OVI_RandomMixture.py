from __future__ import print_function
from openturns import *

# BEGIN_TEX
# Create the univariate distributions

# X1 : Exponential(1.5)
X1 = Exponential(1.5)
# X2 : Normal(4,1)
X2 = Normal(4, 1)

# Put them in a DistributionCollection
distribList = [X1, X2]

# Create the numerical of the distribution weights
# coefficients a1, a2
weight = NumericalPoint([5., 1.])

# Create the constant coefficient a0
a0 = 2.0

# Create the Random Mixture Y = a0 + Sum(ai Xi)
myRandomMixtureY = RandomMixture(distribList, weight, a0)

# Or create the Random Mixture where a0 = 0 : Y = Sum(ai Xi)
myRandomMixtureY = RandomMixture(distribList, weight, a0)

# Or create the Random Mixture where all the weights (a1, a2)are equal to 1
myRandomMixtureY = RandomMixture(distribList, a0)

# Ask myRandomMixtureY its  mean, variance, quantile of order 0.9, its
# probability to exceeds 3
mean = myRandomMixtureY.getMean()[0]
variance = myRandomMixtureY.getCovariance()[0, 0]
quantile90 = myRandomMixtureY.computeQuantile(0.90)[0]
proba = myRandomMixtureY.computeComplementaryCDF(3.0)

# Ask myRandomMixtureY to draw its pdf
pdfY = myRandomMixtureY.drawPDF()

# Visualize the graph without saving it
# View(pdfY).show()

# Transform the RandomMixture into a RandomVector
myRandomVectorY = RandomVector(myRandomMixtureY)
# END_TEX
