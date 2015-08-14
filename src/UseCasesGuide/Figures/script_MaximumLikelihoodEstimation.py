from openturns import *
from math import *

# Compute the log-likelihood instead of the likelihood to avoid underflow
# By the way, we are obliged to truncate it to avoid computing log(0)...
class LogLikelihoodFunction(OpenTURNSPythonFunction):

  def __init__(self, sample):
    OpenTURNSPythonFunction.__init__(self, 2, 1)
    self.sample_ = sample

  def _exec(self, X):
    normal=Normal(X[0], X[1])
    logLikelihood = 0.0
    # The PDF is assume to be constant, equals to eps for values smaller than eps
    eps = 1.0e-16
    for i in range(self.sample_.getSize()) :
      pdf = normal.computePDF(self.sample_[i])
      if (pdf > eps):
        logLikelihood = logLikelihood + log(pdf)
      else:
        logLikelihood = logLikelihood + log(eps)
        return [logLikelihood]


#Create a sample from Normal(mu = 2,sigma = 1)
size = 10000
sample = Normal(2,1).getSample(size)

# Create the Python functionpython associated to the sample
myLogLikelihoodPython = LogLikelihoodFunction(sample)

# Create the NumericalMathFunction of the library openturns
myLogLikelihoodOT = NumericalMathFunction(myLogLikelihoodPython)

# Create the research interval of (mu, sigma)
lowerBound = NumericalPoint(2)
lowerBound[0] = -1
lowerBound[1] = 1.0e-4
upperBound = NumericalPoint(2)
upperBound[0] = 3
upperBound[1] = 2
finiteLowerBound = BoolCollection(2)
finiteLowerBound[0] = 0
finiteLowerBound[1] = 1
finiteUpperBound = BoolCollection(2)
finiteUpperBound[0] = 0
finiteUpperBound[1] = 0
bounds = Interval(lowerBound, upperBound, finiteLowerBound, finiteUpperBound)

# Create the starting point of the research
# For mu : the first point
# For sigma : a value evaluated from the two first data
startingPoint = NumericalPoint(2)
startingPoint[0] = sample[0][0]
startingPoint[1] = sqrt((sample[1][0] - sample[0][0])*(sample[1][0] - sample[0][0]))
print "Starting point=", startingPoint

# Create the TNC algorithm
myAlgoTNC = TNC(TNCSpecificParameters(), myLogLikelihoodOT, bounds, startingPoint, BoundConstrainedAlgorithmImplementationResult.MAXIMIZATION)

# Run the algorithm and extract results
myAlgoTNC.run()
resMLE = BoundConstrainedAlgorithm(myAlgoTNC).getResult()
MLEparameters = resMLE.getOptimizer()
print "MLE of (mu, sigma) = (", MLEparameters[0], ", ", MLEparameters[1], ")"
dist = NormalFactory().build(sample)
parameters = dist.getParametersCollection()[0]
print "OT estimate = (", parameters[0], ", ", parameters[1], ")"
