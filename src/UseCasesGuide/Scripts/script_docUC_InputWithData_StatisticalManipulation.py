from __future__ import print_function
from openturns import *

# Generate a sample of dimension 3
sample = Normal(3).getSample(500)

# Get min and max per component
print("Min per component =", sample.getMin())
print("max per component =", sample.getMax())

# Get the range per component
# range = max - min
print("Range per component =", sample.computeRange())

# Get the mean per component
print("Mean =", sample.computeMean())

# Get the standard deviation per component
print("Standard deviation per component =",
      sample.computeStandardDeviationPerComponent())

# BEGIN_TEX
# Get the Variance per component
print("Variance =", sample.computeVariance())

# Get the Skewness per component
print("Skewness =", sample.computeSkewness())

# Get the Kurtosis per component
print("Kurtosis =", sample.computeKurtosis())

# Get the median per component
print("Median per component =", sample.computeMedian())

# Get the empirical 0.95 quantile per component
print("0.95 quantile per component =",
      sample.computeQuantilePerComponent(0.95))

# Get the sample covariance
print("Covariance =", sample.computeCovariance())

# Get the sample standard deviation
print("Standard deviation =", sample.computeStandardDeviation())

# Get the sample  Pearson correlation matrix
print("Pearson correlation =", sample.computePearsonCorrelation())

# Get  the sample Kendall correlation matrix
print("Kendall correlation =", sample.computeKendallTau())

# Get  the sample Spearman  correlation matrix
print("Spearman correlation =", sample.computeSpearmanCorrelation())

# Get the value of the empirical CDF at a point
# For ex in dimension 3
myPoint = NumericalPoint([1.1, 2.2, 3.3])
print("Empirical CDF at point POINT = ", sample.computeEmpiricalCDF(myPoint))

# Get the value of the empirical CDF at point POINT
print("Empirical CDF at point POINT = ",
      sample.computeEmpiricalCDF(myPoint, True))

# END_TEX
