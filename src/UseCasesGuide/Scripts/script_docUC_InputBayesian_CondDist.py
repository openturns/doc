from __future__ import print_function
from openturns import *

# BEGIN_TEX
# Create the conditioned distribution
conditionedDist = Uniform()

# Create the conditioning distribution
conditioningDist = Uniform(-1.0, 1.0)

# Create the ling function g
g = NumericalMathFunction(['y'], ['y', '1+y^2'])

# Create the resulting conditional distribution
finalDist = ConditionalDistribution(conditionedDist, conditioningDist, g)

# Generate some realizations
sampleY = finalDist.getSample(1000)
# END_TEX
