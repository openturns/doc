from __future__ import print_function
from openturns import *

# CONTINUOUS distributions

# BEGIN_TEX
##########
# Arcsine
##########

# Ppal Param: Arcsine(a, b)
arcsine = Arcsine(5.0, 11.0)
# Param 1 : (mu, sigma) is coded by 1
arcsine = Arcsine(0.0, 1.0, 1)
# It is also possible to write :
arcsine = Arcsine(0.0, 1.0, Arcsine.MUSIGMA)
# Default construction => Arcsine() = Arcsine(-1.0, 1.0)
arcsine = Arcsine()

##########
# Beta
##########

# Ppal Param : Beta(r, t, a, b)
beta = Beta(2.0, 3.0, 0.0, 2.0)
# Param 1 : (mu, sigma, a, b) is coded by 1
beta = Beta(1.0, 0.5, 0.0, 2.0, 1)
# It is also possible to write :
beta = Beta(1.0, 0.5, 0.0, 2.0, Beta.MUSIGMA)
# Default construction ==> Beta(r, t, a, b)= Beta(2, 4, -1, 1)
beta = Beta()

##########
# Burr
##########

# Ppal Param: Burr(c,k)
burr = Burr(1.5, 2.7)
# Default construction =>  Burr(c,k) = (1.0, 1.0)
burr = Burr()

##########
# Chi
##########

# Ppal Param: Chi(nu)
chi = Chi(1.5)
# Default construction => Chi(nu) = Chi(1.0)
chi = Chi()

##########
# ChiSquare
##########

# Ppal Param: ChiSquare(nu)
chiSquare = ChiSquare(1.5)
# Default construction => ChiSquare(nu) = ChiSquare(1.0)
chiSquare = ChiSquare()

##########
# Dirac 1D
##########

# Ppal Param: Dirac(p) = Dirac([p])
dirac = Dirac(1.5)  # = Dirac([1.5])
# Default construction => Dirac() = Dirac(0.0)
dirac = Dirac()
# Dirac 2D
# Ppal Param: Dirac(point) = Dirac([p_1, ..., p_n])
dirac = Dirac([0.5, 1.2])

##########
# Dirichlet bivariate
##########

# Ppal Param: Dirichlet([teta_1, theta_2, theta_3])
dirichlet = Dirichlet([1.5, 2.3, 3.4])
# Default construction => Dirichlet() = Dirichlet([1.0, 1.0])
dirichlet = Dirichlet()

##########
# Epanechnikov
##########

# No parameter
# Default construction
epanechnikov = Epanechnikov()

##########
# Exponential
##########

# Ppal Param : Exponential(lambda, gamma)
exponential = Exponential(1.0, 2.0)
# Default construction ==> Exponential(lambda, gamma) = Exponential(1.0, 0.0)
exponential = Exponential()

##########
# FisherSnedecor
##########

# Ppal Param : FisherSnedecor(d1,d2)
fisherSnedecor = FisherSnedecor(100, 100)
# Default construction ==> FisherSnedecor(d1,d2) = FisherSnedecor(1,1)
fisherSnedecor = FisherSnedecor()

##########
# Gamma
##########

# Ppal Param : Gamma(k, lambda, gamma)
gamma = Gamma(3.0, 1.0, 2.0)
# Param 1 : (mu, sigma, gamma) is coded by 1
gamma = Gamma(3.0, 1.0, 2.0, 1)
# It is also possible to write :
gamma = Gamma(3.0, 1.0, 2.0, Gamma.MUSIGMA)
# Default construction ==> Gamma(k, lambda, gamma) = Gamma(1.0, 1.0, 0.0)
gamma = Gamma()

##########
# Generalized Pareto Distribution
##########

# Ppal Param : GeneralizedPareto(sigma, xi)
gpd = GeneralizedPareto(2.4, 0.3)

##########
# Gumbel
##########

# Ppal Param : Gumbel(alpha, beta)
gumbel = Gumbel(1.0, 2.0)
# Param 1 : (mu, sigma) is coded by 1
gumbel = Gumbel(1.0, 2.0, 1)
# It is also possible to write :
gumbel = Gumbel(1.0, 2.0, Gumbel.MUSIGMA)
# Default construction ==> Gumbel(alpha, beta) = Gumbel(1.0, 1.0)
gumbel = Gumbel()

##########
# Histogram
##########

# Example : n = 3, x1 = 0.0 and
# (li,hi)_{i=1, ..., 3} = (1.0, 1.0), (4.0, 2.0), (2.0, 3.0)
# The heights (hi) are automatically renormalized
# Ppal Param : Histogram(x1, (li,hi)_{i=1, ..., n})
collection = HistogramPairCollection(((1.0, 1.0), (4.0, 2.0), (2.0, 3.0), ))
histogram = Histogram(0.0, collection)

##########
# InverseGamma
##########

# Ppal Param : InverseGamma(k,lambda)
inverseGamma = InverseGamma(1, 2)
# Default construction ==> InverseGamma(k, lambda) = InverseGamma(1.0, 1.0)
inverseGamma = InverseGamma()

##########
# InverseNormal
##########

# Ppal Param : InverseNormal(lambda, mu)
inverseNormal = InverseNormal(1, 2)
# Default construction ==> InverseNormal(lambda, mu) = InverseNormal(1.0, 1.0)
inverseNormal = InverseNormal()

##########
# InverseWishart
##########

# Ppal Param : InverseWishart(V, nu)
V = CovarianceMatrix(2)
V[0, 0] = 2.0
V[1, 0] = 1.0
V[1, 1] = 3.0
nu = 3.5
inverseWishart = InverseWishart(V, nu)
# Default construction ==> InverseWishart(V, nu) = InverseWishart(Id_1, 1.0)
inverseWishart = InverseWishart()

##########
# Laplace
##########

# Ppal Param : Laplace(lambda, mu)
laplace = Laplace(2, 0.5)
# Default construction ==> Laplace(lambda, mu) = Laplace(1.0, 0.0)
laplace = Laplace()

##########
# Logistic
##########

# Ppal Param : (alpha, beta)
logistic = Logistic(1.0, 2.0)
# Default construction ==> Logistic(alpha, beta) = Logistic(0.0, 1.0)
logistic = Logistic()

##########
# LogNormal
##########

# Ppal Param : LogNormal(mu_l, sigma_l,gamma)
lognormal = LogNormal(3.0, 2.0, 1.0)
# Param 1 : (mu, sigma, gamma) is coded by 1
lognormal = LogNormal(3.0, 2.0, 1.0, 1)
# It is also possible to write :
lognormal = LogNormal(3.0, 2.0, 1.0, LogNormal.MUSIGMA)
# Param 2 : (mu, sigma/mu, gamma, 2) is coded by 2
lognormal = LogNormal(3.0, 2.0, 1.0, 2)
# It is also possible to write :
lognormal = LogNormal(3.0, 2.0, 1.0, LogNormal.MU_SIGMAOVERMU)
# Default construction ==> LogNormal(mu_l, sigma_l,gamma) = LogNormal(0.0,
# 1.0, 0.0)
logNormal = LogNormal()

# LogUniform
# Ppal Param : LogUniform(mu_l, sigma_l,gamma)
logUniform = LogUniform(1.0, 2.0)
# Default construction ==> LogNormal(mu_l, sigma_l,gamma) = LogNormal(0.0,
# 1.0, 0.0)
logUniform = LogUniform()

##########
# MeixnerDistribution
##########

# Ppal Param : MeixnerDistribution(alpha, beta, delta, mu)
meixnerDistribution = MeixnerDistribution(2.0, 0.5, 1.3, 0.1)
# Default construction ==> MeixnerDistribution(alpha, beta, delta, mu) =
# MeixnerDistribution(1,0,1,0)
meixnerDistribution = MeixnerDistribution()


##########
# Non Central Chi Square
##########

# Ppal Param : NonCentralChiSquare(nu, lambda)
nonCentralChiSquare = NonCentralChiSquare(3.0, 2.0)
# Default construction ==> NonCentralChiSquare(nu, delta, gamma) =
# NonCentralChiSquare(5,0)
nonCentralChiSquare = NonCentralChiSquare()


##########
# Non Central Student
##########

# Ppal Param : NonCentralStudent(nu, delta, gamma) =
# NonCentralStudent(3.0, 1.0, 0.0)
nonCentralStudent = NonCentralStudent(3.0, 1.0, 0.0)
# Default construction ==> NonCentralStudent(nu, delta, gamma) =
# NonCentralStudent(5.0, 0.0, 0.0)
nonCentralStudent = NonCentralStudent()

##########
# Normal(1D)
##########

# Ppal Param : Normal(mu, sigma) = Normal(2.0, 1.0)
normal1D = Normal(2.0, 1.0)
# Default construction ==> 1D Normal distribution with zero mean and unit
# variance :
normal1D_standard = Normal()

##########
# NormalGamma(2D)
##########

# Ppal Param : NormalGamma(mu, kappa, alpha, beta) = NormalGamma(1.0, 2.0,
# 1.0, 1.0)
myNormalGamma = NormalGamma(1.0, 2.0, 1.0, 1.0)
# Default construction ==> (mu, kappa, alpha, beta) = (0, 1, 1, 1)
normal1D_standard = NormalGamma()

##########
# Normal (nD)
##########

# Ppal Param  : Normal(mu, sigma, R)
normal2D_1 = Normal(
    NumericalPoint(2, 1.0), NumericalPoint(2, 2.0), CorrelationMatrix(2))
# Param 2 : Normal(mu, C)
myCovarianceMatrix = CovarianceMatrix(2)
myCovarianceMatrix[0, 0] = 1.0
myCovarianceMatrix[0, 1] = 0.7
myCovarianceMatrix[1, 0] = 0.7
myCovarianceMatrix[1, 1] = 2.0
normal2D_2 = Normal(NumericalPoint(2, 1.0), myCovarianceMatrix)
# 2D Normal distribution with zero mean and identity covariance matrix:
normal2D_standard = Normal(2)

# In order to create a Normal of dimension n
# with 0 mean and Identity variance matrix
n = 5
normalStandardnD = Normal(n)

##########
# Rayleigh
##########

# Ppal Param : Rayleigh(sigma, gamma)
rayleigh = Rayleigh(2.5, -0.5)
# Default construction ==> Rayleigh(sigma, gamma) = Rayleigh(1.0, 0.0)
rayleigh = Rayleigh()

##########
# Rice
##########

# Ppal Param : Rice(sigma, nu)
rice = Rice(0.5, 2.5)
# Default construction ==> Rice(sigma, nu)= Rice(1.0, 0.0)
rice = Rice()

##########
# Student (1D)
##########

# Ppal Param = Student(nu, mu, sigma)
student = Student(3.0, 2.0, 4.0)
# Default construction ==> Student(nu, mu, sigma) = Student(3.0, 0.0, 1.0)
student = Student()

##########
# Student (nD)
##########

# Ppal Param = Student(nu, mu, sigma, R)
student = Student(
    3.0, NumericalPoint(2, 1.0), NumericalPoint(2, 3.0), CorrelationMatrix(2))
# Default construction nD ==> Student(nu, mu) = Student(nu,
# NumericalPoint(d, 1.0), NumericalPoint(d, 1.0), CorrelationMatrix(d))
student = Student(4.0, 3)

##########
# Trapezoidal
##########

trapezoidal = Trapezoidal(1.0, 2.0, 3.0, 4.0)
# Default construction ==> Trapezoidal(a, b, c, d) = Trapezoidal(-2.0,
# -1.0, 1.0, 2.0)
trapezoidal = Trapezoidal()

##########
# Triangular
##########

# Ppal Param = Triangular(a,m,b)
triangular = Triangular(1.0, 2.0, 4.0)
# Default construction ==> Triangular(a, m, b) = Triangular(-1.0, 0.0, 1.0)
triangular = Triangular()

##########
# TruncatedNormal
##########

# Ppal Param  = TruncatedNormal(mu_n, sigma_n, a, b)
truncatednormal = TruncatedNormal(1.0, 2.0, -1.0, 5.0)
# Default construction ==> TruncatedNormal(mu_n, sigma_n, a, b) =
# TruncatedNormal(0.0, 1.0, -1.0, 1.0)
TruncatedNormal = TruncatedNormal()

##########
# Uniform
##########

# Ppal Param = Uniform(a,b)
uniform = Uniform(1.0, 2.0)
# Default construction ==> Uniform(a,b) = Uniform(-1.0, 1.0)
uniform = Uniform()

##########
# Weibull
##########

# Ppal Param = Weibull(e, beta, gamma)
weibull = Weibull(1.0, 2.0, 3.0)
# Param 1 = (mu, sigma, gamma) is coded by 1
weibull = Weibull(4.0, 2.0, 3.0, 1)
# It is also possible to write :
weibull = Weibull(4.0, 2.0, 3.0, Weibull.MUSIGMA)
# Default construction ==> Weibull(e, beta, gamma) = Weibull(1.0, 1.0, 0.0)
weibull = Weibull()

##########
# Wishart
##########

# Ppal Param : Wishart(V, nu)
V = CovarianceMatrix(2)
V[0, 0] = 2.0
V[1, 0] = 1.0
V[1, 1] = 3.0
nu = 3.5
wishart = Wishart(V, nu)
# Default construction ==> Wishart(V, nu) = Wishart(Id_1, 1.0)
wishart = Wishart()


# DISCRETE distributions

##########
# Bernoulli
##########

# Ppal Param : Bernoulli(p)
# Default construction ==> Bernoulli(p) =  Bernoulli(0.5)
bernoulli = Bernoulli(0.3)

##########
# Binomial
##########

# Ppal Param : Binomial(n,p)
# Default construction ==>  Binomial(n,p) =  Binomial(1,0.5)
binomial = Binomial(5, 0.7)

##########
# KPermutationsDistribution
##########

# Ppal Param : KPermutationsDistribution(k,n)
# Default construction ==>  KPermutationsDistribution() =
# KPermutationsDistribution(1,1)
kpermutations = KPermutations(2, 3)

##########
# Geometric
##########

# Ppal Param : Geometric(p)
# Default construction ==>  Geometric(p) =  Geometric(0.5)
geometric = Geometric(0.3)

##########
# Multinomial
##########

# Ppal Param : Multinomial(N, (p_i)_{i=1, ..., n})
multinomial = Multinomial(5, NumericalPoint(4, 0.25))

##########
# NegativeBinomial
##########

# Ppal Param : NegativeBinomial(r,p)
# Default construction ==>  NegativeBinomial(r,p) =  NegativeBinomial(1,0.5)
negativeBinomial = NegativeBinomial(5, 0.7)

##########
# Poisson
##########

# Ppal Param : Poisson(lambda)
# Default construction ==>  Poisson(lambda) =  Poisson(1)
poisson = Poisson(0.3)

##########
# Skellam
##########

# Ppal Param : Skellan(lambda1, lambda2)
# Default construction ==>  Skellan(lambda1, lambda2)=Skellan(1.,1.)
skellam = Skellam(1.2, 3.4)


##########
# UserDefined (nD), n=2
##########

# We create a collection of pair (xi, pi), i=1,2,3, each xi in R^2
# Weights are not complusory normalized to 1
# OpenTURNS automatically normalizes them

# Give the range of the distribution
# First pair : (x1 = (1.0, 1.5), p1 = 3)
# Second pair : (x2 = (2.0, 2.5), p2 = 3)
# Third pair : (x3 = (3.0, 3.5), p3 = 4)
range = NumericalSample([[1.0, 1.5], [2.0, 2.5], [3.0, 3.5]])

# Give the list of the respective weights
# First pair :  p1 = 3
# Second pair : p2 = 3
# Third pair : p3 = 4
weights = NumericalPoint([3, 3, 4])


# Create the UserDefined distribution
distribution = UserDefined(range, weights)

##########
# ZipfMandelbrot
##########

# Ppal Param : ZipfMandelbrot(N,q,s)
# Default construction ==>  ZipfMandelbrot(N,q,s) = ZipfMandelbrot(1,0,1)
zipfMandelbrot = ZipfMandelbrot(3, 0.3, 2.4)
# END_TEX
