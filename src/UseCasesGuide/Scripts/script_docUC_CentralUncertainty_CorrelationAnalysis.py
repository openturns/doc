from __future__ import print_function
from openturns import *

# Create the model Y = x1^2 + x2
model = NumericalMathFunction(["x1", "x2"], ["y"], ["x1^2+x2"])

inputDist = ComposedDistribution(
    DistributionCollection([Normal(), Normal()]), IndependentCopula(2))
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
output = RandomVector(model, inputVector)

# Generate the input sample
N = 500
inputSample = inputVector.getSample(N)
inputSample2 = inputSample.getMarginal(0)

# Evaluate the associated output sample
outputSample = model(inputSample)
outputSample.setDescription(["Y"])

# BEGIN_TEX
# PCC coefficients evaluated between the outputSample and each coordinate
# of inputSample
PCCcoefficient = CorrelationAnalysis.PCC(inputSample, outputSample)
print('PCC coefficients = ', PCCcoefficient)

# PRCC evaluated between the outputSample and each coordinate of
# inputSample (based on the rank values)
PRCCcoefficient = CorrelationAnalysis.PRCC(inputSample, outputSample)
print('PRCC coeffcieints = ', PRCCcoefficient)

# SRC evaluated between the outputSample and each coordinate of inputSample
SRCcoefficient = CorrelationAnalysis.SRC(inputSample, outputSample)
print('SRC coefficients = ', SRCcoefficient)

# SRRC evaluated between the outputSample and each coordinate of
# inputSample (based on the rank values)
SRRCcoefficient = CorrelationAnalysis.SRRC(inputSample, outputSample)
print('SRRC coefficients = ', SRRCcoefficient)

# Pearson Correlation Coefficient
# CARE :  inputSample must be of dimension 1
pearsonCorrelation = CorrelationAnalysis.PearsonCorrelation(
    inputSample2, outputSample)
print('Pearson correlation = ', pearsonCorrelation)

# Spearman Correlation Coefficient
# CARE :  inputSample must be of dimension 1
spearmanCorrelation = CorrelationAnalysis.SpearmanCorrelation(
    inputSample2, outputSample)
print('Spearman correlation = ', spearmanCorrelation)
# END_TEX
