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

sampleSize = 250

X = distribution.getSample(sampleSize)
Y = myModel(X)

# BEGIN_TEX
dimension = X.getDimension()

# build the orthogonal basis
coll = []
for i in range(dimension):
    coll.append(
        StandardDistributionPolynomialFactory(distribution.getMarginal(i)))
enumerateFunction = LinearEnumerateFunction(dimension)
productBasis = OrthogonalProductPolynomialFactory(coll, enumerateFunction)

# create the algorithm
degree = 6
adaptiveStrategy = FixedStrategy(
    productBasis, enumerateFunction.getStrataCumulatedCardinal(degree))
projectionStrategy = LeastSquaresStrategy()
algo = FunctionalChaosAlgorithm(
    X, Y, distribution, adaptiveStrategy, projectionStrategy)
algo.run()

# get the metamodel function
result = algo.getResult()
metamodel = result.getMetaModel()

# END_TEX
print((result.getResiduals()))
