from openturns import *
from scriptExample_elasticTruss_PhysicalModel  import *
from scriptExample_elasticTruss_ProbaModel import *
from numpy import empty, argmin, array, arange, floor, sqrt, linspace
from pylab import ion, figure, semilogy, xlabel, ylabel, bar, legend, xticks, yticks, hist
#
# Model function
#
truss_model = NumericalMathFunction(myfunction())
#
# Output random vector
#
vectY = RandomVector(truss_model, vectX)
#
# Basis of the polynomial chaos (PC) expansion (Hermite polynomials are selected)
#
polyColl = PolynomialFamilyCollection(dim)
for i in range(dim):
    polyColl[i] = HermiteFactory()
#
enumerateFunction = LinearEnumerateFunction(dim)
multivariateBasis = OrthogonalProductPolynomialFactory(polyColl,enumerateFunction)
#
# Definition of the approx. algo.: Least Angle Regression (LAR)
#
basisSequenceFactory = LAR()
fittingAlgorithm = CorrectedLeaveOneOut()
approximationAlgorithm = LeastSquaresMetaModelSelectionFactory(basisSequenceFactory,fittingAlgorithm)
#
# Number of simulations (i.e. simulation budget)
#
N = 200
#
# Initialization of the seed of the random generator
RandomGenerator.SetSeed(77)
#
evalStrategy = LeastSquaresStrategy(LHSExperiment(N),approximationAlgorithm)
#
# Parametric study varying the PC degree
#
pmax = 4
Results_tuple = ()
Relative_errors = empty(pmax)
p_list = range(1,pmax+1)
#
for p in p_list:
    #
    P = enumerateFunction.getStrataCumulatedCardinal(p)
    truncatureBasisStrategy = FixedStrategy(multivariateBasis,P)
    #
    polynomialChaosAlgorithm = FunctionalChaosAlgorithm (truss_model, \
    Distribution(myDistribution) , truncatureBasisStrategy, evalStrategy)
    polynomialChaosAlgorithm.run()
    #
    new_result = polynomialChaosAlgorithm.getResult()
    Results_tuple = Results_tuple + (new_result,)
    #
    Relative_errors[p-1] = array(new_result.getRelativeErrors())[0]
#
# Plot the obtained relative errors
ion()
lw = 2.5
figure(1)
semilogy(p_list,Relative_errors,linewidth=lw)
xticks(list(arange(pmax)+1))
xlabel('PC degree') ; ylabel('Relative corrected leave-one-out error')
#
# Identify the most accurate PC expansion
p_optim = argmin(Relative_errors) + 1
The_Result = Results_tuple[p_optim-1]
#
print "" ; print "Optimal degree: ", p_optim
print "" ; print "Relative corrected LOO error:", Relative_errors[p_optim-1]
print "" ; print "Number of nonzero coefficients:", len(The_Result.getIndices())
#
# Post-processing of the optimal PC expansion
#
ChaosRV = FunctionalChaosRandomVector(The_Result)
#
Mean = ChaosRV.getMean()[0]
StD = sqrt(ChaosRV.getCovariance()[0,0])
print "" ; print "Response mean: ", Mean ; print ""
print "" ; print "Response standard deviation: ", StD ; print ""
#
SU = empty(dim) ; SUT = empty(dim)
for i in range(dim):
    SU[i] = ChaosRV.getSobolIndex(i)
    SUT[i] = ChaosRV.getSobolTotalIndex(i)
#
# Plot the sensitivity indices
w = 0.4
figure(2)
b1 = bar((arange(dim)+1)-w,SU,width=w,color='#000999')
b2 = bar((arange(dim)+1),SUT,width=w,color='#66FFFF')
legend((b1[0],b2[0]),('Sobol indices','Total Sobol indices'),'upper left')
xticks(list(arange(dim)+1),(r'$E_1$',r'$E_2$',r'$E_3$',r'$S_1$',r'$S_2$',r'$S_3$',r'$P$',r'$\theta$',r'$\alpha_1$',r'$\alpha_2$'),size=18)
yticks(list( linspace(0.,1.,5) ))
#
#Plot histogram
truss_model_PC = The_Result.getMetaModel()
#
samplesize = 100000
sample_X = vectX.getSample(samplesize)
sample_YPC = truss_model_PC(sample_X)
asampleYPC = array(sample_YPC).flatten()
#
figure(3)
hist(asampleYPC,normed=True,bins=floor(sqrt(samplesize)))
xlabel("Displacement (m)", fontsize=14)
ylabel("Relative frequency", fontsize=14)
#
print "" ; print "Skewness:",  sample_YPC.computeSkewnessPerComponent()[0] ; print ""
print "" ; print "Kurtosis:",  sample_YPC.computeKurtosisPerComponent()[0] ; print ""
