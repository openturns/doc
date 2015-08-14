from __future__ import print_function
from openturns import *

# Generate a sample from a continous distribution
sample_cont = Beta(1.2, 3.2, 0.0, 1.0).getSample(100)

# Generate a sample from a discrete distribution
sample_disc = Geometric(0.8).getSample(500)

# BEGIN_TEX
################################
# Case 1 : Continuous distribution
################################

# Fit a Beta distribution to the sample
estimatedBeta = BetaFactory().build(sample_cont)

# Get the parameters of the estimated distribution
estimatedParam = estimatedBeta.getParametersCollection()

# Display the resulted distribution with its parameters
print("Estimated Beta distribution=", estimatedBeta)

# Validate the Beta fitted distribution with the Kolmogorov Test
resultKolmogorov = FittingTest.Kolmogorov(sample_cont, estimatedBeta, 0.95)

# Print result of the Kolmogorov Test
print("Test Succes ? ", (resultKolmogorov.getBinaryQualityMeasure() == 1))

# Get the p-value of the Kolmogorov Test
print("p-value of the Kolmogorov Test = ", resultKolmogorov.getPValue())

# Get the p-value threshold of the Kolmogorov Test
print("p-value threshold = ", resultKolmogorov.getThreshold())

# Validate the Beta fitting with a visual test : QQ-plot test
# Generate the Graph structure for the QQ-plot graph
# number of points of the graph fixed to 100 (20 by default)
sampleBetaQQPlot = VisualTest.DrawQQplot(sample_cont, estimatedBeta)

# To visualize the graph
# View(sampleBetaQQPlot).show()

# Draw the graph on files
sampleBetaQQPlot.draw("SampleBetaQQPlot")

################################
# Case 2 : Discrete distribution
################################

# Fit a  Geometric distribution to the sample
estimatedGeom = GeometricFactory().build(sample_disc)

# Display the resulted distribution with its parameters
print("Estimated Geometric distribution=", estimatedGeom)

# Validate the Geometric fitted distribution with the Chi-squared Test
resultChiSquared = FittingTest.ChiSquared(sample_disc, estimatedGeom, 0.95)
# END_TEX
