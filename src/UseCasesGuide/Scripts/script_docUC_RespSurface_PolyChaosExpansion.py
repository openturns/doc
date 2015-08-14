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

# BEGIN_TEX
#############################################################
# STEP 1 : Construction of the multivariate orthonormal basis
#############################################################

# Dimension of the input random vector
dim = 4

# Create the univariate polynomial family collection
# which regroups the polynomial families for each direction
polyColl = PolynomialFamilyCollection(dim)
# For information, with the Krawtchouk and Charlier families :
polyColl[0] = KrawtchoukFactory()
polyColl[1] = CharlierFactory()
# for information, with the automatic selection
for i in range(Xdist.getDimension()):
    polyColl[i] = StandardDistributionPolynomialFactory(Xdist.getMarginal(i))
# We overload these factories as they are dedicated to discrete distributions
polyColl[0] = HermiteFactory()
polyColl[1] = LegendreFactory()
polyColl[2] = LaguerreFactory(2.75)
# Parameter for the Jacobi factory : 'Probabilty' encoded with 1
polyColl[3] = JacobiFactory(2.5, 3.5, 1)

# Create the enumeration function
# LinearEnumerateFunction
enumerateFunction = LinearEnumerateFunction(dim)

# HyperbolicAnisotropicEnumerateFunction
q = 0.4
enumerateFunction_1 = HyperbolicAnisotropicEnumerateFunction(dim, q)

# Create the multivariate orthonormal basis
# which is the the cartesian product of the univariate basis
multivariateBasis = OrthogonalProductPolynomialFactory(
    polyColl, enumerateFunction)

# Ask how many polynomials have degrees equal to k=5
k = 5
print(enumerateFunction.getStrataCardinal(k))

# Ask how many polynomials have degrees inferior or equal to k=5
print(enumerateFunction.getStrataCumulatedCardinal(k))

# Give the k-th term of the multivariate basis
# To calculate its degree, add the integers
k = 5
print(enumerateFunction(k))

# Build a term of the basis as a NumericalMathFunction
# Generally, we do not need to construct manually any term,
# all terms are constructed automatically by a strategy of construction of
# the basis
i = 5
Psi_i = multivariateBasis.build(i)

# Get the measure mu associated to the multivariate basis
distributionMu = multivariateBasis.getMeasure()

####################################################################
# STEP 2 : Truncature strategy of the multivariate orthonormal basis
#############################################################
# FixedStrategy :
# all the polynomials af degree <=2
# which corresponds to the 15 first ones
p = 15
truncatureBasisStrategy = FixedStrategy(multivariateBasis, p)

# SequentialStrategy :
# among the maximumCardinalBasis = 100 first polynomials
# of the multivariate basis those verfying the convergence criterion,
maximumCardinalBasis = 100
truncatureBasisStrategy_1 = SequentialStrategy(
    multivariateBasis, maximumCardinalBasis)

# CleaningStrategy :
# among the maximumConsideredTerms = 500 first polynomials,
# those which have the mostSignificant = 50 most significant contributions
# with significance criterion significanceFactor = 10^(-4)
# The True boolean indicates if we are interested
# in the online monitoring of the current basis update
# (removed or added coefficients)
maximumConsideredTerms = 500
mostSignificant = 50
significanceFactor = 1.0e-4
truncatureBasisStrategy_2 = CleaningStrategy(
    multivariateBasis, maximumConsideredTerms, mostSignificant, significanceFactor, True)

################################################################
# STEP 3 : Evaluation strategy of the approximation coefficients
#############################################################
# The technique illustrated is the Least Squares technique
# where the points come from an design of experiments
# Here : the Monte Carlo sampling technique
sampleSize = 100
evaluationCoeffStrategy = LeastSquaresStrategy(
    MonteCarloExperiment(sampleSize))

# You can specify the approximation algorithm
# This is the algorithm that generates a sequence of basis using Least
# Angle Regression
basisSequenceFactory = LAR()

# This algorithm estimates the empirical error on each sub-basis using
# Leave One Out strategy
fittingAlgorithm = CorrectedLeaveOneOut()
# Finally the metamodel selection algorithm embbeded in LeastSquaresStrategy
approximationAlgorithm = LeastSquaresMetaModelSelectionFactory(
    basisSequenceFactory, fittingAlgorithm)
evaluationCoeffStrategy_2 = LeastSquaresStrategy(
    MonteCarloExperiment(sampleSize), approximationAlgorithm)

# Try integration
marginalDegrees = [2] * dim
evaluationCoeffStrategy_3 = IntegrationStrategy(
    GaussProductExperiment(distributionMu, marginalDegrees))

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
# END_TEX
