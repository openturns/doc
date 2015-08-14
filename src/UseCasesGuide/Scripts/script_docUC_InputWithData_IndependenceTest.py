from __future__ import print_function
from openturns import *

# Generate two discrete samples
discSample1 = Poisson(0.2).getSample(100)
discSample2 = Poisson(0.2).getSample(100)

# Generate two continuous samples
contSample1 = Normal().getSample(100)
contSample2 = Normal().getSample(100)


# BEGIN_TEX
#############################
# ChiSquared Independance test
# Are both scalar samples independent ?
#############################

# Care : discrete distributions only
# H0 = independent samples
# p-value threshold : probability of the H0 reject zone : 1-0.90
# p-value : probability (test variable decision > test variable decision evaluated on the samples)
# Test = True <=> p-value > p-value threshold
resultChiSquared = HypothesisTest.ChiSquared(discSample1, discSample2, 0.90)

# Print result of the ChiSquared Test
print("Test Succes ? ", (resultChiSquared.getBinaryQualityMeasure() == 1))

# Get the p-value of the  Test
print("p-value of the  Test = ", resultChiSquared.getPValue())

# Get the p-value threshold of the ChiSquared Test
print("p-value threshold = ", resultChiSquared.getThreshold())

#############################
# Pearson Test
# Are both scalar samples independent ?
#############################

# Care : samples are supposed to form a gaussian vector
# The test is based on the evaluation of the linear correlation coefficient
# H0 : independent samples (linear correlation coefficient = 0)
resultPearson = HypothesisTest.Pearson(contSample1, contSample2, 0.90)


#############################
# Spearman Test
# Have both scalar samples a monotonous relation
#############################

# H0 : no monotonous relation between both samples
resultSpearman = HypothesisTest.Spearman(contSample1, contSample2, 0.90)

# END_TEX
