from __future__ import print_function
from openturns import *

# BEGIN_TEX
# Create the first marginal : Weibul(mu, sigma, gamma) = Weibull(2.0, 1.0, 0.0)
weibDist = Weibull(2.0, 1.0, 0.0, Weibull.MUSIGMA)
weibDist.setName("myWeibull")

# Create the second marginal : Triangular(a,m,b) = Triangular(1.0, 3.0, 5.0)
triangularDist = Triangular(1.0, 3.0, 5.0)
triangularDist.setName("myTriangular")

# Create the third marginal : Uniform(a,b) = Uniform(2.0, 4.0)
uniformDist = Uniform(2.0, 4.0)
uniformDist.setName("myUniform")

# Create a collection of distribution of dimension 3
# using List python
aCollection = [weibDist, triangularDist, uniformDist]

#############################
# CASE 1 : independent copula
#############################
# It is not necessary to specify the copula
# Create the distribution
# Create a collection of distribution of dimension 3
# using List python
myDistribution = ComposedDistribution(aCollection)

#############################
# CASE 2 : other copula
#############################
# Create a copula : Normal copula of dimension 3 fom Spearman rank
# correlation matrix
spearmanMatrix = CorrelationMatrix(3)
spearmanMatrix[0, 1] = 0.25
spearmanMatrix[1, 2] = 0.25
aCopula = NormalCopula(
    NormalCopula.GetCorrelationFromSpearmanCorrelation(spearmanMatrix))
aCopula.setName("Normal copula")

# Create the distribution
myDistribution = ComposedDistribution(aCollection, aCopula)

# Give a Description to the Distribution
myDistribution.setDescription(("dist1", "dist2", "dist3"))

# END_TEX
