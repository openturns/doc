#! /usr/bin/env python
from __future__ import print_function
from openturns import *

# Create a function R^n --> R^p
# For example R^4 --> R
myModel = NumericalMathFunction(
    ['x1', 'x2', 'x3', 'x4'], ['y'], ['1+x1*x2 + 2*x3^2+x4^4'])

# Create a distribution of dimension n
# for example n=3 with indpendent components
distribution = ComposedDistribution(
    [Normal(), Uniform(), Gamma(2.75, 1.0), Beta(2.5, 3.5, -1.0, 2.0)])

sampleSize = 100

X = distribution.getSample(sampleSize)
Y = myModel(X)

# BEGIN_TEX
dimension = X.getDimension()

# STEP 1: Construction of the autocorrelation function
covarianceModel = SquaredExponential(dimension, 0.1)

# STEP2: Construction of the regression basis
basis = ConstantBasisFactory(dimension).build()

# STEP 3: Construction of the algorithm
algo = KrigingAlgorithm(X, Y, basis, covarianceModel)
algo.run()

# STEP 4: Get the metamodel function
result = algo.getResult()
metamodel = result.getMetaModel()

# END_TEX
print((result.getResiduals()))
