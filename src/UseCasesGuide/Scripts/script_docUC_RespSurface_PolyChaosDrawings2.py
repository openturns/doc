from __future__ import print_function
from openturns import *


# Create a function R^n --> R^p
# For example R^4 --> R
myModel = NumericalMathFunction(
    ['x1', 'x2', 'x3', 'x4'], ['y'], ['1+x1*x2 + 2*x3^2+x4^4'])

# Create a distribution of dimension n
# for example n=3 with indpendent components
Xdist = ComposedDistribution(
    [Normal(), Uniform(), Gamma(2.75, 1.0), Beta(2.5, 3.5, -1.0, 2.0)])

#############################################################
# STEP 1 : Construction of the multivariate orthonormal basis
#############################################################

# Dimension of the input random vector
dim = 4

# Create the univariate polynomial family collection
polyColl = PolynomialFamilyCollection(dim)
# For information, with the Krawtchouk and Charlier families :
polyColl[0] = KrawtchoukFactory()
polyColl[1] = CharlierFactory()
# which regroups the polynomial families for each direction
polyColl = PolynomialFamilyCollection(dim)
polyColl[0] = HermiteFactory()
polyColl[1] = LegendreFactory()
polyColl[2] = LaguerreFactory(2.75, 1)
# Parameter for the Jacobi factory : 'Probabilty' encoded with 1
polyColl[3] = JacobiFactory(2.5, 3.5, 1)


# Create the enumeration function
# LinearEnumerateFunction
enumerateFunction = LinearEnumerateFunction(dim)
# HyperbolicAnisotropicEnumerateFunction
q = 0.4
enumerateFunction = HyperbolicAnisotropicEnumerateFunction(dim, q)

# Create the multivariate orthonormal basis
# which is the the cartesian product of the univariate basis
multivariateBasis = OrthogonalProductPolynomialFactory(
    polyColl, enumerateFunction)


####################################################################
# STEP 2 : Truncature strategy of the multivariate orthonormal basis
#############################################################

# FixedStrategy :
# all the polynomials af degree <=2
# which corresponds to the 15 first ones
p = 15
truncatureBasisStrategy = FixedStrategy(multivariateBasis, p)


################################################################
# STEP 3 : Evaluation strategy of the approximation coefficients
#############################################################

sampleSize = 100
# This is the algorithm that generates a sequence of basis using Least
# Angle Regression
basisSequenceFactory = LAR()
# This algorithm estimates the empirical error on each sub-basis using
# Leave One Out strategy
fittingAlgorithm = CorrectedLeaveOneOut()
# Finally the metamodel selection algorithm embbeded in LeastSquaresStrategy
approximationAlgorithm = LeastSquaresMetaModelSelectionFactory(
    basisSequenceFactory, fittingAlgorithm)
evaluationCoeffStrategy = LeastSquaresStrategy(
    MonteCarloExperiment(sampleSize), approximationAlgorithm)


#####################################################
# STEP 4 : Creation of the Functional Chaos Algorithm
#############################################################
# FunctionalChaosAlgorithm :
# combination of the model : myModel
# the distribution of the input random vector : Xdist
# the truncature strategy of the multivariate basis
# and the evaluation strategy of the coefficients
polynomialChaosAlgorithm = FunctionalChaosAlgorithm(
    myModel, Xdist, truncatureBasisStrategy, evaluationCoeffStrategy)


#####################################################
# Perform the simulation
#####################################################
polynomialChaosAlgorithm.run()

# Stream out the result
polynomialChaosResult = polynomialChaosAlgorithm.getResult()

# Get the meta model which is the composed meta model combined with the
# iso probabilistic transformation
metaModel = polynomialChaosResult.getMetaModel()


# BEGIN_TEX
#####################################################
# GRAPH 2 : points cloud between model and meta model
#####################################################

# Generate a NumericalSample of the input random vector
sizeX = 500
Xsample = Xdist.getSample(sizeX)

# Evaluate the model on the sample
modelSample = myModel(Xsample)

# Evaluate the meta model on the sample
metaModelSample = metaModel(Xsample)

# Create the numerical sample of points (Y, Y_tilde)
sampleMixed = NumericalSample(sizeX, 2)
for i in range(sizeX):
    sampleMixed[i, 0] = modelSample[i, 0]
    sampleMixed[i, 1] = metaModelSample[i, 0]

# Create a fine title
legend = str(sizeX) + " realizations"

# Create the cloud
comparisonCloud = Cloud(sampleMixed, "blue", "fsquare", legend)

# Put it within a graph structure
graphCloud = Graph(
    "Polynomial chaos expansion", "model", "meta model", True, "topleft")

# Fulfill the graph with the cloud
graphCloud.add(comparisonCloud)

# In order to see the graphs
# View(graphCloud).show()
# END_TEX
