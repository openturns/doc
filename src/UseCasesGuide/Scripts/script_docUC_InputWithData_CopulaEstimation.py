from __future__ import print_function
from openturns import *

# Create a bidimensionnal sample
# For example  :
dist = ComposedDistribution(
    DistributionCollection([Normal(), Normal()]), GumbelCopula(3))
N = 500
sample = dist.getSample(N)

# BEGIN_TEX
################################
# Case 1 : Parametric estimation
################################

# Estimate a copula from the  numerical sample
# for example a gumbel model
estimatedParamCop = GumbelCopulaFactory().build(sample)
print("Gumbel Copula  = ", estimatedParamCop)


################################
# Case 2 : Non parametric estimation
################################

# Build a non parametric estimation of
# the multivariate distribution
# For example with the kernel smoothing method
myEstimatedDist = KernelSmoothing().build(sample)

# Then extract the copula
estimatedSklarCop = myEstimatedDist.getCopula()
print("Sklar Copula  = ", estimatedSklarCop)

################################
# Validation in the rank space
################################

# Map the sample into the rank space

# Creation of the operator which transforms the marginals into the uniform ones
# We suppose here that the marginal distributions are both Normal(0,1)
ranksTransf = MarginalTransformationEvaluation(
    DistributionCollection([Normal(), Normal()]), MarginalTransformationEvaluation.FROM)

# Transformation of the initial sample into the ranked sample
rankSample = NumericalSample(sample.getSize(), sample.getDimension())
for i in range(sample.getSize()):
    rankSample[i] = ranksTransf(sample[i])

# Cloud in the rank space
rankCloud = Cloud(rankSample, 'blue', 'plus', 'sample')
myGraph = Graph(
    'Parametric estimation of the copula', 'X', 'Y', True, 'topleft')
myGraph.setLegendPosition('bottomright')
myGraph.add(rankCloud)

# Then draw the iso-curves of the estimated copula
minPoint = NumericalPoint([0.0, 0.0])
maxPoint = NumericalPoint([1.0, 1.0])
pointNumber = Indices([201, 201])
graphCop = estimatedParamCop.drawPDF(minPoint, maxPoint, pointNumber)
contour_estCop = graphCop.getDrawable(0)

# Erase the labels of the iso-curves
contour_estCop.setDrawLabels(False)

# Change the levels of the iso-curves
# Levels of the iso curves
nlev = 31
levels = NumericalPoint(nlev)
for i in range(nlev):
    levels[i] = 0.25 * nlev / (1.0 + i)
    contour_estCop.setLevels(levels)

# Change the legend of the curves
contour_estCop.setLegend('Gumbel copula')

# Change the color of the iso-curves
contour_estCop.setColor('red')

# Add the iso-curves graph into the cloud one
myGraph.add(contour_estCop)

# Visualize the graph
# View(myGraph).show()

# END_TEX
