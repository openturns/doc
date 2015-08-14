from __future__ import print_function
from openturns import *

# Create the model (x1,x2) --> (y1,y2) = (x1^2 + x2, x2^2+x1)
model = NumericalMathFunction(
    ["x1", "x2"], ["y1", "y2"], ["x1^2+x2", "x2^2+x1"])

inputDist = ComposedDistribution(
    DistributionCollection([Normal(), Normal()]), IndependentCopula(2))
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
output = RandomVector(model, inputVector)

size = 10000
inputSample1 = inputDist.getSample(size)
inputSample2 = inputDist.getSample(size)

try:
    # use non-interactive backend
    import matplotlib
    matplotlib.use('Agg')
except:
    pass

# BEGIN_TEX
# Initialize computation
sensitivityAnalysis = SensitivityAnalysis(inputSample1, inputSample2, model)

# Allow multithreading if available
sensitivityAnalysis.setBlockSize(int(ResourceMap.Get("parallel-threads")))

# Compute second order indices (first, second and total order indices are
# computed together)
secondOrderIndices = sensitivityAnalysis.getSecondOrderIndices()

# Retrieve first order indices
firstOrderIndices = sensitivityAnalysis.getFirstOrderIndices()

# Retrieve total order indices
totalOrderIndices = sensitivityAnalysis.getTotalOrderIndices()

# Print some indices
print("First order Sobol indice of Y|X1 = %.6f" % firstOrderIndices[0])
print("Total order Sobol indice of Y|X3 = %.6f" % totalOrderIndices[1])
print("Second order Sobol indice of Y|X1,X3 = %.6f" % secondOrderIndices[0, 1])

# Draw first order indices
s1 = NumericalPointWithDescription(firstOrderIndices)
s1.setDescription(inputDist.getDescription())
ifPlot = sensitivityAnalysis.DrawImportanceFactors(s1)
ifPlot.setTitle("First Order Sensitivity Indices")
try:
    from openturns.viewer import View
    View(ifPlot).show()
except:
    pass
    # END_TEX
