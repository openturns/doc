from __future__ import print_function
from openturns import *

# Example in dimension 3

# Create the amplitude vector :
# amplitude = (1., 2., 3.)
amplitude = [1.0, 2.0, 3.0]

# scale = (4., 5., 6.)
scale = [4.0, 5.0, 6.0]

# spatialCorrelation
spatialCorrelation = CorrelationMatrix(3)
spatialCorrelation[0, 1] = 0.8
spatialCorrelation[0, 2] = 0.6
spatialCorrelation[1, 2] = 0.1

# spatialCovariance
spatialCovariance = CovarianceMatrix(3)
spatialCovariance[0, 0] = 4.0
spatialCovariance[1, 1] = 5.0
spatialCovariance[2, 2] = 6.0
spatialCovariance[0, 1] = 1.2
spatialCovariance[0, 2] = 0.9
spatialCovariance[1, 2] = -0.2

# BEGIN_TEX
# Create the spectral model
# for example : the Cauchy model

# from the amplitude, scale and spatialCovariance
mySpectralModel_Corr = CauchyModel(amplitude, scale, spatialCorrelation)

# or from the scale and spatialCovariance
mySpectralModel_Cov = CauchyModel(scale, spatialCovariance)
# END_TEX
