from openturns import *
from openturns.viewer import View



class modelePYTHON(OpenTURNSPythonFunction) :
  # that following method defines the input size (4) and the output size (1)
  def __init__(self) :
    OpenTURNSPythonFunction.__init__(self, 4, 1)

  # that following method gives the implementation of modelePYTHON
  def _exec(self,x) :
    E=x[0]
    F=x[1]
    L=x[2]
    I=x[3]
    return [-(F*L*L*L)/(3.*E*I)]

# Use that function defined in the script python
# with the openturns library
# Create a NumericalMathFunction from modelePYTHON
modelePoutre = NumericalMathFunction(modelePYTHON())

# Create the input random distribution of (E,F,L,I)
distributionE = Beta(0.9, 3.2, 2.8e7, 4.9e7)
# distributionF.getK() = 2.78
# distributionF.getLambda() = 0.000185

distributionF = Gamma(30000.0, 9000.0, 15000, Gamma.MUSIGMA)

distributionL = Uniform(250, 260)

distributionI = Beta(2.5,4.0,3.1e2,4.5e2)

collectionMarginales = DistributionCollection(4)
collectionMarginales[0] = distributionE
collectionMarginales[1] = distributionF
collectionMarginales[2] = distributionL
collectionMarginales[3] = distributionI

copule = IndependentCopula(4)

inputDistribution = ComposedDistribution(collectionMarginales, copule)

# Create the input random vecrtor (E,F,L,I)
inputRandomVector = RandomVector(inputDistribution)

# Cretae the ouput variable of interest
outputVariable = RandomVector(modelePoutre, inputRandomVector)

#############################################################
# STEP 1 : Construction of the multivariate orthonormal basis

# Dimension of the input random vector
dim = inputRandomVector.getDimension()

# Create the univariate polynomial family collection
# which regroups the polynomial families for each direction
polyColl = PolynomialFamilyCollection(dim)

#Jacobi(alpha, beta) <=> Beta(\beta + 1, \alpha + \beta + 2, -1, 1)
alphaJ = 1.3
betaJ = -0.1
jacobiFamily = JacobiFactory(alphaJ, betaJ)
polyColl[0] = jacobiFamily

# Laguerre(k) <=> Gamma(k+1,1,0) (parametrage ppal)
kLaguerre = 1.78
laguerreFamily = LaguerreFactory(kLaguerre)
polyColl[1] = OrthogonalUniVariatePolynomialFamily(laguerreFamily)

# Legendre <=> Unif(-1,1)
legendreFamily = LegendreFactory()
polyColl[2] = legendreFamily

# Jacobi(alpha, beta) <=> Beta(\beta + 1, \alpha + \beta + 2, -1, 1)
alphaJ2 = 0.5
betaJ2 = 1.5
jacobiFamily2 = JacobiFactory(alphaJ2, betaJ2)
polyColl[3] = jacobiFamily2


# Create the multivariate orthonormal basis
# which is the the cartesian product of the univariate basis
multivariateBasis = OrthogonalProductPolynomialFactory(polyColl, LinearEnumerateFunction(dim))

# Build a term of the basis as a NumericalMathFunction
# Generally, we do not need to construct manually any term,
# all terms are constructed automatically by a strategy of construction of the basis
i=5
Psi_i = multivariateBasis.build(i)

# Get the measure mu associated to the multivariate basis
distributionMu = multivariateBasis.getMeasure()

####################################################################
# STEP 2 : Truncature strategy of the multivariate orthonormal basis

# FixedStrategy :
# all the polynoms af degree <=2
# which corresponds to the 15 first ones
p = 50
truncatureBasisStrategy = FixedStrategy(multivariateBasis, p)

# SequentialStrategy :
### among the maximumCardinalBasis = 100 first polynoms
### of the multivariate basis those verfying the convergence criterion,
##maximumCardinalBasis = 100
##truncatureBasisStrategy = SequentialStrategy(multivariateBasis, maximumCardinalBasis)


# CleaningStrategy :
# among the maximumConsideredTerms = 500 first polynoms,
# those which have the mostSignificant = 50 most significant contributions
# with significance criterion significanceFactor = 10^(-4)
# The True boolean indicates if we are interested
# in the online monitoring of the current basis update
# (removed or added coefficients)
maximumConsideredTerms = 500
mostSignificant = p
significanceFactor = 1.0e-4
truncatureBasisStrategy = CleaningStrategy(multivariateBasis, maximumConsideredTerms, mostSignificant, significanceFactor, True)


################################################################
# STEP 3 : Evaluation strategy of the approximation coefficients

# The technique proposed is the Least Squares technique
# where the points come from an experiment plane
# Here : the Monte Carlo sampling technique
sampleSize = 100
evaluationCoeffStrategy = LeastSquaresStrategy(MonteCarloExperiment(sampleSize))

# STEP 4 : Creation of the Functional Chaos Algorithm

# FunctionalChaosAlgorithm :
# combination of the model : limitStateFunction
# the distribution of the input random vector : Xdistribution
# the truncature strategy of the multivariate basis
# and the evaluation strategy of the coefficients
polynomialChaosAlgorithm = FunctionalChaosAlgorithm(modelePoutre, inputDistribution, truncatureBasisStrategy, evaluationCoeffStrategy)

#########################################################
# Run and results exploitation

# Perform the simulation
polynomialChaosAlgorithm.run()

# Stream out the result
polynomialChaosResult = polynomialChaosAlgorithm.getResult()

# Get the polynomial chaos coefficients
coefficients = polynomialChaosResult.getCoefficients()

# Get the meta model as a NumericalMathFunction
metaModel = polynomialChaosResult.getMetaModel()

# Get the multivariate basis
# as a colletion of NumericalMathFunction
multivariateBasisCollection = polynomialChaosResult.getReducedBasis()

# Get the distribution of variables Z
mu = polynomialChaosResult.getOrthogonalBasis().getMeasure()

# Get the composed model which is the model of the reduced variables Z
composedModel = polynomialChaosResult.getComposedModel()

########################################
# Graphs validation
########################################

# Graph 1 : cloud

# Generate a NumericalSample of the input random vector
# Evaluate the meta model and the real model
# draw the coulds (metamodel, real model)
# Verify points are on the first diagonal
sizeX = 500
Xsample = inputDistribution.getSample(sizeX)

modelSample = modelePoutre(Xsample)
metaModelSample = metaModel(Xsample)

legend = str(sizeX) + " realizations"
comparisonCloud = Cloud(modelSample, metaModelSample)
comparisonCloud.setColor("blue")
comparisonCloud.setPointStyle("fsquare")
comparisonCloud.setLegend(legend)
graphCloud = Graph("Polynomial chaos expansion", "model", "meta model", True, "topleft")
graphCloud.add(comparisonCloud)
xMin = min(modelSample.getMin()[0], metaModelSample.getMin()[0])
xMax = min(modelSample.getMax()[0], metaModelSample.getMax()[0])
data = NumericalSample(0, 2)
data.add(NumericalPoint([xMin, xMin]))
data.add(NumericalPoint([xMax, xMax]))
diagonal = Curve(data)
diagonal.setColor("red")
graphCloud.add(diagonal)

#View(graphCloud).show()
graphCloud.draw("PCE_comparisonModels")


# Graph 2 : polynoms family graphs

degreeMax = 5
pointNumber = 101
colorList = Drawable.GetValidColors()

# Jacobi for E
xMinJacobi = -1
xMaxJacobi = 1
titleJacobi = "Jacobi(" + str(alphaJ) + ", " + str(betaJ) + ") polynomials"
graphJacobi = Graph(titleJacobi, "z", "polynomial values", True, "topleft")
for i in range(degreeMax) :
  graphJacobi_temp = jacobiFamily.build(i).draw(xMinJacobi, xMaxJacobi, pointNumber)
  graphJacobi_temp_draw = graphJacobi_temp.getDrawable(0)
  legend = "degree " + str(i)
  graphJacobi_temp_draw.setLegend(legend)
  graphJacobi_temp_draw.setColor(colorList[i])
  graphJacobi.add(graphJacobi_temp_draw)
  #View(graphJacobi).show()
  graphJacobi.draw("PCE_JacobiPolynomials_VariableE")

# Laguerre for F
xMinLaguerre = 0
xMaxLaguerre = 10
titleLaguerre = "Laguerre(" + str(kLaguerre) +  ") polynomials"
graphLaguerre = Graph(titleLaguerre, "z", "polynomial values", True, "topleft")
for i in range(degreeMax) :
  graphLaguerre_temp = laguerreFamily.build(i).draw(xMinLaguerre, xMaxLaguerre, pointNumber)
  graphLaguerre_temp_draw = graphLaguerre_temp.getDrawable(0)
  legend = "degree " + str(i)
  graphLaguerre_temp_draw.setLegend(legend)
  graphLaguerre_temp_draw.setColor(colorList[i])
  graphLaguerre.add(graphLaguerre_temp_draw)
  #View(graphLaguerre).show()
  graphLaguerre.draw("PCE_LaguerrePolynomials_VariableF")

# Legendre for L
xMinLegendre = -1
xMaxLegendre = 1
titleLegendre = "Legendre polynomials"
graphLegendre = Graph(titleLegendre, "z", "polynomial values", True, "topright")
for i in range(degreeMax) :
  graphLegendre_temp = laguerreFamily.build(i).draw(xMinLegendre, xMaxLegendre, pointNumber)
  graphLegendre_temp_draw = graphLegendre_temp.getDrawable(0)
  legend = "degree " + str(i)
  graphLegendre_temp_draw.setLegend(legend)
  graphLegendre_temp_draw.setColor(colorList[i])
  graphLegendre.add(graphLegendre_temp_draw)
  #View(graphLegendre).show()
  graphLegendre.draw("PCE_LegendrePolynomials_VariableL")

# Jacobi for I
xMinJacobi2 = -1
xMaxJacobi2 = 1
titleJacobi2 = "Jacobi(" + str(alphaJ2) + ", " + str(betaJ2) + ") polynomials"
graphJacobi2 = Graph(titleJacobi2, "z", "polynomial values", True, "topright")
for i in range(degreeMax) :
  graphJacobi2_temp = jacobiFamily2.build(i).draw(xMinJacobi2, xMaxJacobi2, pointNumber)
  graphJacobi2_temp_draw = graphJacobi2_temp.getDrawable(0)
  legend = "degree " + str(i)
  graphJacobi2_temp_draw.setLegend(legend)
  graphJacobi2_temp_draw.setColor(colorList[i])
  graphJacobi2.add(graphJacobi2_temp_draw)
  #View(graphJacobi2).show()
  graphJacobi2.draw("PCE_JacobiPolynomials_VariableI")


###########################################
# Graphs of the Krawtchouk(5,0.6) family

# Krawtchouk(N,p) <==> Binomial(N,p)
N = 5
p=0.6
krawtchoukFamily = KrawtchoukFactory(N,p)

xMinKrawtchouk = -1
xMaxKrawtchouk = 5

titleKrawtchouk = "Krawtchouk(" + str(N) + ", " + str(p) + ") polynomials"
graphKrawtchouk = Graph(titleKrawtchouk, "z", "polynomial values", True, "topright")
for i in range(degreeMax) :
  graphKrawtchouk_temp = krawtchoukFamily.build(i).draw(xMinKrawtchouk, xMaxKrawtchouk, pointNumber)
  graphKrawtchouk_temp_draw = graphKrawtchouk_temp.getDrawable(0)
  legend = "degree " + str(i)
  graphKrawtchouk_temp_draw.setLegend(legend)
  graphKrawtchouk_temp_draw.setColor(colorList[i])
  graphKrawtchouk.add(graphKrawtchouk_temp_draw)

#View(graphKrawtchouk).show()
graphKrawtchouk.draw("PCE_KrawtchoukPolynomials")



###########################################
# Graphs of theCharlier(5,0.6) family

#Charlier(lambda) <=> Poisson(lambda)
l = 0.6
charlierFamily =CharlierFactory(l)

xMinCharlier = -1
xMaxCharlier = 5

titleCharlier = "Charlier(" + str(l) + ") polynomials"
graphCharlier = Graph(titleCharlier, "z", "polynomial values", True, "bottomleft")
for i in range(degreeMax) :
  graphCharlier_temp = charlierFamily.build(i).draw(xMinCharlier, xMaxCharlier, pointNumber)
  graphCharlier_temp_draw = graphCharlier_temp.getDrawable(0)
  legend = "degree " + str(i)
  graphCharlier_temp_draw.setLegend(legend)
  graphCharlier_temp_draw.setColor(colorList[i])
  graphCharlier.add(graphCharlier_temp_draw)

#View(graphCharlier).show()
graphCharlier.draw("PCE_CharlierPolynomials")
