from __future__ import print_function
from openturns import *

# Generate a sample of dimension 2
mean = NumericalPoint(4)
sigma = NumericalPoint(4, 1.0)
corrMat = CorrelationMatrix(4)
corrMat[0, 1] = 0.8
corrMat[0, 2] = 0.8
corrMat[0, 3] = 0.8
corrMat[1, 2] = 0.8
corrMat[1, 3] = 0.8
corrMat[2, 3] = 0.8
dist4D = Normal(mean, sigma, corrMat)

sample = dist4D.getSample(100)
sample1 = sample.getMarginal([0, 1, 2])
sample2 = sample.getMarginal(3)

# BEGIN_TEX
#########################
# Partial Pearson Test :
# Are both samples independent?
#########################

# Supposes that both  samples  form a gaussian vector  (based on the evaluation of the linear correlation coefficient)
# H0 : independent samples (linear correlation coefficient = 0)
# Test = True <=> independent samples (linear correlation coefficient = 0)
# p-value threshold : probability of the H0 reject zone : 1-0.90
# p-value : probability (test variable decision > test variable decision evaluated on the samples)
# Test = True <=> p-value > p-value threshold

# selection of components of sample1 to be tested to sample2
# for example, components 1, 2 if sample2.getDimension() >= 2
selection = list(range(2))

# Perform the Partial Pearson Test
resultPartialPearson = HypothesisTest.PartialPearson(
    sample1, sample2, selection, 0.90)

# Print the global result of the Pearson Test
print("Test global result : ", resultPartialPearson)

# Print result of the Pearson Test for each coordinate tested
for i in selection:
    print("Test Succes for Coordinate =  ", selection[i], "? ", (
        resultPartialPearson[i].getBinaryQualityMeasure() == 1))

# Get the p-value of the Pearson Test
print("p-value of the Pearson Test = ", resultPartialPearson[i].getPValue())

# Get the p-value threshold of the  Test
i = 0
print("p-value threshold for Coordinate =  ",
      selection[i], " = ", resultPartialPearson[i].getThreshold())

# Full Pearson Test : it performs the partial Pearson test on the whole
# coordinates of the first sample

#########################
# Full Pearson Test
#########################

resultFullPearson = HypothesisTest.FullPearson(sample1, sample2, 0.90)


#########################
# Partial Spearman Test :
# Have two scalar samples  a monotonous relation
#########################

# H0 : no monotonous relation between both samples

# selection of coordinates of sample1 to be tested to sample2
# for example, components 1, 2 if sample2.getDimension() >= 2
selection = list(range(2))

# Perform the Partial Spearman Test
resultPartialSpearman = HypothesisTest.PartialSpearman(
    sample1, sample2, selection, 0.90)

#########################
# Full Spearman Test
#########################

# it performs the partial Pearson test on the whole composnents of the
# first sample

# Perform the Full Spearman Test
resultFullSpearman = HypothesisTest.FullSpearman(sample1, sample2, 0.90)
# END_TEX
