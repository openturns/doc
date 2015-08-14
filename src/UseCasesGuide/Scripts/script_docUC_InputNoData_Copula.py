from __future__ import print_function
from openturns import *

# BEGIN_TEX
######################
# ALIMIKHAILHAQ copula
######################

# For example, theta = -0.5
theta = -0.5
amhCopula = AliMikhailHaqCopula(theta)

################
# CLAYTON copula
################

# Only for dimension = 2
theta = -0.5
claytonCopula = ClaytonCopula(theta)

#################
# COMPOSED copula
#################

# For example, the GumbelCopula concatenated to a Clayton one
# Create the collection of copulas with default parameters
finalCopula = ComposedCopula([GumbelCopula(), ClaytonCopula()])

###########################
# FARLIE MORGENSTEIN copula
###########################

# For example, theta = 0.5
theta = 0.5
fgm = FarlieGumbelMorgensternCopula(theta)

##############
# FRANK copula
##############

# Only for dimension = 2
# Frank copula is parameterized by theta without restriction
# For example, theta = 9.2
theta = 9.2
frankCopula = FrankCopula(theta)

###############
# GUMBEL copula
###############

# Only for dimension = 2
# Gumbel copula is parameterized by theta without restriction
# For example, theta = 2.5
theta = 2.5
gumbelCopula = GumbelCopula(theta)

####################
# INDEPENDENT copula
####################

# Independent Copula parameterized by its dimension
# For example, dimension = 3
dim = 3
independentCopula = IndependentCopula(dim)

############
# MIN Copula
############

# For example, dimension = 3
dim = 3
minCopula = MinCopula(dim)

################
# NORMAL copula
################

################
# Case 1 :
# Normal Copula parameterized by its correlation matrix R

# For example, dimension = 3
dim = 3
R = CorrelationMatrix(dim)
for i in range(dim - 1):
    R[i, i + 1] = 0.8

# It is possible to define the correlation matrix through a map
# and then use the function getCorrelationMatrixFromMap to convert
# the map into a CorrelationMatrix
# if input variables are noted X,Y and Z
vars = ['X', 'Y', 'Z']
correlationMap = {}
correlationMap['X'] = {}
correlationMap['X']['X'] = 1.0
correlationMap['X']['Y'] = 0.8
correlationMap['X']['Z'] = 0.8
correlationMap['Y'] = {}
correlationMap['Y']['X'] = 0.8
correlationMap['Y']['Y'] = 1.0
correlationMap['Y']['Z'] = 0.8
correlationMap['Z'] = {}
correlationMap['Z']['X'] = 0.8
correlationMap['Z']['Y'] = 0.8
correlationMap['Z']['Z'] = 1.0
R = getCorrelationMatrixFromMap(vars, correlationMap)

# Create a normal copula from the correlation matrix R
normalCopula = NormalCopula(R)
normalCopula.setName("a normal copula")

################
# Case 2 :
# Create a normal copula from the Spearman rank correlation matrix S

# For example, dimension = 3
dim = 3
S = CorrelationMatrix(dim)
for i in range(1, dim):
    S[i, i - 1] = 0.25

# Create the correlation matrix R of the  normal copula
# from the Spearman correlation matrix S
R = NormalCopula.GetCorrelationFromSpearmanCorrelation(S)

# Create the normal copula from the R correlation matrix
normalCopula = NormalCopula(R)
normalCopula.setName("another normal copula")

################
# Case 3 :
# Normal Copula parameterized by its dimension

# Correlation matrix R is equal to identity
dim = 3
normalCopula = NormalCopula(dim)

##############
# SKLAR Copula
##############

# For example, the copula of a 2d Student distribution
# Student(nu, mu, sigma, R)
myStudent = Student(
    3.0, NumericalPoint(2, 1.0), NumericalPoint(2, 3.0), CorrelationMatrix(2))
sklarCopula = SklarCopula(myStudent)

####################
# MIXTURE of copulas
####################

# For example, the mixture of a GumbelCopula and a Clayton one
# with parameters 0.2 and 0.6
copulaList = [GumbelCopula(4.5), ClaytonCopula(2.3)]
parameters = [0.2, 0.6]
# Create the mixture of copulas
finalCopula = Mixture(copulaList, parameters)
print(finalCopula.isCopula())

########################
# ORDINAL SUM of copulas
########################

# For example, a GumbelCopula and a NormalCopula
# in dimension 2 with default parameters
# where the GumbelCopula is squeezed in [0,0.3]
# where the NormalCopula is squeezed in [0.3, 1]
ordinalSumCop = OrdinalSumCopula([GumbelCopula(2), NormalCopula(2)], [0.3])
# END_TEX
