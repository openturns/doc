from __future__ import print_function
import openturns as ot
import math as m

# Generate a scalar sample
sample = ot.Normal().getSample(200)

# BEGIN_TEX
# Compute the log-likelihood instead of the likelihood to avoid underflow
# and truncate it to avoid computing log(0)...


class LogLikelihoodFunction(ot.OpenTURNSPythonFunction):

    def __init__(self, sample):
        ot.OpenTURNSPythonFunction.__init__(self, 2, 1)
        self.sample_ = sample

    def _exec(self, X):
        normal = ot.Normal(X[0], X[1])
        logLikelihood = 0.0
        # The PDF is assumed to be constant, equal to eps for values smaller
        # than eps
        for i in range(self.sample_.getSize()):
            pdf = normal.computeLogPDF(self.sample_[i])
        return [logLikelihood]


# Create the Python function associated to the sample
# We suppose we have a numerical sample of data : sample
myLogLikelihoodPython = LogLikelihoodFunction(sample)

# Create the NumericalMathFunction of the library openturns
myLogLikelihoodOT = ot.NumericalMathFunction(myLogLikelihoodPython)

# Create the research interval of (mu, sigma)
lowerBound = ot.NumericalPoint((-1.0, 1.0e-4))
upperBound = ot.NumericalPoint((3.0, 2.0))
finiteLowerBound = ot.BoolCollection((0, 1))
finiteUpperBound = ot.BoolCollection((0, 0))
bounds = ot.Interval(lowerBound, upperBound, finiteLowerBound, finiteUpperBound)

# Create the starting point of the research
# For mu : the first point
# For sigma : a value evaluated from the two first data
startingPoint = ot.NumericalPoint(2)
startingPoint[0] = sample[0][0]
startingPoint[1] = m.sqrt(
    (sample[1][0] - sample[0][0]) * (sample[1][0] - sample[0][0]))

# Create the optimization problem
problem = ot.OptimizationProblem(myLogLikelihoodOT, ot.NumericalMathFunction(), ot.NumericalMathFunction(), bounds)
problem.setMinimization(False)

# Create the TNC algorithm
myAlgoTNC = ot.TNC(problem)
myAlgoTNC.setStartingPoint(startingPoint)

# Run the algorithm and extract results
myAlgoTNC.run()
resMLE = myAlgoTNC.getResult()
MLEparameters = resMLE.getOptimalPoint()
print("MLE of (mu, sigma) = (", MLEparameters[0], ", ", MLEparameters[1], ")")
# END_TEX
