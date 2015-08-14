from __future__ import print_function
from openturns import *

# Create the Ishigami model
formulaIshigami = Description(1)
formulaIshigami[
    0] = "sin(_pi*X1)+7*sin(_pi*X2)*sin(_pi*X2)+0.1*((_pi*X3)*(_pi*X3)*(_pi*X3)*(_pi*X3))*sin(_pi*X1)"

model = NumericalMathFunction(["X1", "X2", "X3"], ["y"], formulaIshigami)

# Create an independant distribution
distributions = ComposedDistribution([Uniform(-1.0, 1.0)] * 3)

# BEGIN_TEX
# Initialize computation of the indices
sensitivityAnalysis = FAST(model, distributions, 400)
# Compute the first order indices (first and total order indices are
# computed together)
firstOrderIndices = sensitivityAnalysis.getFirstOrderIndices()
# Retrieve total order indices
totalOrderIndices = sensitivityAnalysis.getTotalOrderIndices()

# Print indices
print("First order FAST indice of Y|X1 = %.6f" % firstOrderIndices[0])
print("Total order FAST indice of Y|X3 = %.6f" % totalOrderIndices[2])

    # END_TEX
