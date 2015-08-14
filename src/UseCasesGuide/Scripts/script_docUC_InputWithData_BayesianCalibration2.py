#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from openturns import *
import math as m

# Number of covariates
covNum = 1
# Dimension of the observations
obsDim = 1
# Dimension of the vector of parameters to calibrate
paramDim = 3

# The data:
obsSize = 10

# 1) Covariate values
x = NumericalSample(obsSize, covNum)
for i in range(obsSize):
    x[i, 0] = -2 + 5.0 * i / 9.0

# 2) Observations
y_obs = NumericalSample(obsSize, obsDim)
y_obs[0, 0] = -9.50794871493506
y_obs[1, 0] = -3.83296694500105
y_obs[2, 0] = -2.44545713047953
y_obs[3, 0] = 0.0803625289211318
y_obs[4, 0] = 1.01898069723583
y_obs[5, 0] = 0.661725805623086
y_obs[6, 0] = -1.57581204592385
y_obs[7, 0] = -2.95308465670895
y_obs[8, 0] = -8.8878164296758
y_obs[9, 0] = -13.0812290405651

# The likelihood:

# 1) Parametric function which associates, for each observation, some given
#    values of the parameters theta to calibrate to the parameters of the
#    distribution of the corresponding observation
p = NumericalSample(obsSize, paramDim)
for i in range(obsSize):
    for j in range(paramDim):
        p[i, j] = (-2 + 5. * i / 9.) ** j

fullModel = NumericalMathFunction(
    ['p1', 'p2', 'p3', 'x1', 'x2', 'x3'], ['z', 'sigma'], ['p1*x1+p2*x2+p3*x3', '1.0'])
model = NumericalMathFunction(fullModel, list(range(paramDim)))

# 2) Conditional distribution of the observations
#    (here: centered unit normal distribution)
conditional = Normal()

# Finally: the prior distribution
sigma0 = NumericalPoint(paramDim, 10.0)  # standard deviations
C0 = CorrelationMatrix(paramDim)       # variance matrix
for i in range(paramDim):
    C0[i, i] = sigma0[i] * sigma0[i]

m0 = NumericalPoint(paramDim, 0.0)      # mean
prior = Normal(m0, C0)

# BEGIN_TEX

# Additional inputs for the random walk Metropolis-Hastings
# sampler constructor:

# 1) Initial state: the prior mean
theta0 = prior.getMean()

# 2) Proposal distribution: uniform
proposal = DistributionCollection()
for i in range(paramDim):
    proposal.add(Uniform(-1.0, 1.0))

# Creation of the Random Walk Metropolis-Hastings (RWMH) sampler
RWMHsampler = RandomWalkMetropolisHastings(
    prior, conditional, model, p, y_obs, theta0, proposal)

# Tuning of the RWMH algorithm:

# 1) Strategy of calibration for the random walk (trivial example: default)
strategy = CalibrationStrategyCollection(paramDim)
RWMHsampler.setCalibrationStrategyPerComponent(strategy)

# 2) Other parameters
RWMHsampler.setVerbose(True)
RWMHsampler.setThinning(1)
RWMHsampler.setBurnIn(2000)

# Ready to generate a sample from the posterior distribution
# of the parameters theta
sampleSize = 10000
sample = RWMHsampler.getSample(sampleSize)

# Look at the acceptance rate
# (basic checking of the efficiency of the tuning;
# value close to 0.2 usually recommended)
print('acceptance rate=', end=' ')
print(RWMHsampler.getAcceptanceRate())

# It is possible to create a random vector based on the RWMHsampler
myRandomVector = PosteriorRandomVector(RWMHsampler)

# END_TEX
