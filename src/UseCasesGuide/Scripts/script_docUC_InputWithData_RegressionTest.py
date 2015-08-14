from __future__ import print_function
from openturns import *

# Generate a scalar sample sampleY
N = 1000
Xsample = Normal(3).getSample(N)
Ysample = NumericalSample(N, 1)
for i in range(N):
    value = 0.5 + Xsample[i][0] + 2 * Xsample[i][1] + \
        3 * Xsample[i][0] + Normal().getRealization()[0]
    Ysample[i] = NumericalPoint([value])

# BEGIN_TEX
###########################################
# Partial Regression Test between 2 samples :
###########################################

# firstSample of dimension n and secondSample of dimension 1. If
# firstSample[i] is i-th marginal of the firstSample , $PartialRegression$
# performs the linear regression test simultaneously on all firstSample[i]
# and secondSample, for i in the selection. The linear regression test
# tests if the regression model between two scalar numerical samples is
# significant. It is based on the deviation analysis of the regression.
# The Fisher distribution is used.

# selection of components  of sample1 to be tested to sample2
# for example, components 1, 2 (suppose n>5)
selection = list(range(2))

# Perform the Partial Regression Test
resultPartialRegression = HypothesisTest.PartialRegression(
    Xsample, Ysample, selection, 0.90)

# Print the global result of the Regression Test
print("Test global result : ", resultPartialRegression)

# Print result of the Regression Test for each coordinate tested
for i in selection:
    print("Test Succes for Coordinate =  ", selection[i], "? ", (
        resultPartialRegression[i].getBinaryQualityMeasure() == 1))

# Get the p-value of the Regression Test
print("p-value of the Regression Test = ",
      resultPartialRegression[i].getPValue())

# Get the p-value threshold of the  Test
print("p-value threshold for Coordinate =  ",
      selection[i], " = ", resultPartialRegression[i].getThreshold())

###########################################
# Full Regression Test
###########################################

# It performs the partial  Regression test on the whole components of the
# first sample

# Perform the Full Regression  Test
resultFullRegression = HypothesisTest.FullRegression(Xsample, Ysample, 0.90)
# END_TEX
