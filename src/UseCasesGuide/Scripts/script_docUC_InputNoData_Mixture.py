from __future__ import print_function
from openturns import *

# Create the  distributions
# Triangular(1.0, 2.0, 4.0)
dist1 = Triangular(1.0, 2.0, 4.0)
# Normal(-1.0, 1.0)
dist2 = Normal(-1.0, 1.0)

# Create the  copulas
cop1 = GumbelCopula(4.5)
cop2 = ClaytonCopula(2.3)

# BEGIN_TEX
############################################
# CASE 1: Create a mixture of distributions

# Create the collection of distributions
aCollection = [dist1, dist2]

# Create the collection of the weights
myWeights = [0.20, 0.80]

# Create the mixture
myMixture = Mixture(aCollection, myWeights)

# Alternate definition of the weights, not normalized
myWeights2 = [2.0, 5.0]
# The normalization is done automatically
myMixture2 = Mixture(aCollection, myWeights)


############################################
# CASE 2: Create a mixture of copulas

# Create the collection of copulas
aCollection = [cop1, cop2]

# Create the collection of the weights
myWeights = [0.20, 0.80]

# Create the mixture
myMixture = Mixture(aCollection, myWeights)
# END_TEX
