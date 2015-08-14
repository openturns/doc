from __future__ import print_function
from openturns import *

# Generate a scalar sample
sample = Normal().getSample(200)

# BEGIN_TEX
###################
# Henry line graph
###################

# Generate the Graph structure for the Henry line graph
henryPlot = VisualTest.DrawHenryLine(sample)

# To visualize the graph
# View(henryPlot).show()

# Draw the graph on files
# if the file adress is not fulfilled, the file is created in the current
# directory
henryPlot.draw("HenryPlot")

###################
# Anderson Darling Test
###################
# Test = True <=> the sample follows a Normal distribution (H0 hypothesis)
# p-value threshold : probability of the H0 reject zone = 1-0.95
# p-value : probability (test variable decision > test variable decision evaluated on the samples)
# Test = True (=1) <=> p-value > p-value threshold
# Number of parameters estimated from sample : 4
resultAndersonDarling = NormalityTest.AndersonDarlingNormal(sample, 0.95)

# Print result of the  Anderson Darling Test
print("Test Succes ? ", (resultAndersonDarling.getBinaryQualityMeasure() == 1))

# Get the p-value of the Anderson Darling Test
print("p-value of the Anderson Darling Test = ",
      resultAndersonDarling.getPValue())

# Get the p-value threshold of the Anderson Darling Test
print("p-value threshold = ", resultAndersonDarling.getThreshold())

###################
# Cramer Von Mises Test
###################
# H0 hypothesis : the sample follows a Normal distribution
resultCramerVonMises = NormalityTest.CramerVonMisesNormal(sample, 0.95)
# END_TEX
