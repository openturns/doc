from openturns import *

# Uncertain parameters
distribution = Normal(3)
# Model
inputVar = Description(["x", "y", "z"])
formulas = Description(["5*(x+1)^2-2*y*z+3*z"])
outputVar = Description(["out"])
f = NumericalMathFunction(inputVar, formulas)
# Must activate the history mechanism if one want to perform sensitivity analysis
f.enableHistory()
# Sampling
size = 10000
inputSample = distribution.getSample(size)
outputSample = f(inputSample)
comparisonOperator = Less()
threshold = 3.0
ResourceMap.SetAsUnsignedLong("SimulationSensitivityAnalysis-DefaultSampleMargin", 100)
algo = SimulationSensitivityAnalysis(inputSample, outputSample, distribution.getIsoProbabilisticTransformation(), comparisonOperator, threshold)
# Perform the analysis
print "Mean point in event domain=", algo.computeMeanPointInEventDomain()
print "Importance factors at ", threshold, " =", algo.computeImportanceFactors()
print "Importance factors at ", threshold / 2, " =", algo.computeImportanceFactors(threshold / 2)
importanceFactorsGraph = algo.drawImportanceFactors()
importanceFactorsGraph.draw("importanceFactorsGraphSample" + comparisonOperator.getClassName())
print "postscript=", importanceFactorsGraph.getPostscript()
print "bitmap=", importanceFactorsGraph.getBitmap()
# Importance factors evolution on probability scale
importanceFactorsRangeGraphProbability = algo.drawImportanceFactorsRange()
importanceFactorsRangeGraphProbability.draw("importanceFactorsRangeGraphProbabilitySample" + comparisonOperator.getClassName())
print "postscript=", importanceFactorsRangeGraphProbability.getPostscript()
print "bitmap=", importanceFactorsRangeGraphProbability.getBitmap()
# Importance factors evolution on threshold scale
importanceFactorsRangeGraphThreshold = algo.drawImportanceFactorsRange(False)
importanceFactorsRangeGraphThreshold.draw("importanceFactorsRangeGraphThresholdSample" + comparisonOperator.getClassName())
print "postscript=", importanceFactorsRangeGraphThreshold.getPostscript()
print "bitmap=", importanceFactorsRangeGraphThreshold.getBitmap()

# Reset the history of the model
f.clearHistory()

# Analysis based on an event
X = RandomVector(distribution)
Y = RandomVector(f, X)
event = Event(Y, comparisonOperator, threshold)
# Get a sample of the event to simulate a Monte Carlo analysis. We don't care of the result as the interesting values are stored in the model history
event.getSample(size)
algo = SimulationSensitivityAnalysis(event)
# Perform the analysis
print "Mean point in event domain=", algo.computeMeanPointInEventDomain()
print "Importance factors at threshold ", threshold, " =", algo.computeImportanceFactors()
print "Importance factors at threshold/2 ", threshold / 2, " =", algo.computeImportanceFactors(threshold / 2)
importanceFactorsGraph = algo.drawImportanceFactors()
importanceFactorsGraph.draw("importanceFactorsGraphEvent" + comparisonOperator.getClassName())
print "postscript=", importanceFactorsGraph.getPostscript()
print "bitmap=", importanceFactorsGraph.getBitmap()
# Importance factors evolution on probability scale
importanceFactorsRangeGraphProbability = algo.drawImportanceFactorsRange()
importanceFactorsRangeGraphProbability.draw("importanceFactorsRangeGraphProbabilityEvent" + comparisonOperator.getClassName())
print "postscript=", importanceFactorsRangeGraphProbability.getPostscript()
print "bitmap=", importanceFactorsRangeGraphProbability.getBitmap()
# Importance factors evolution on threshold scale
importanceFactorsRangeGraphThreshold = algo.drawImportanceFactorsRange(False)
importanceFactorsRangeGraphThreshold.draw("importanceFactorsRangeGraphThresholdEvent" + comparisonOperator.getClassName())
print "postscript=", importanceFactorsRangeGraphThreshold.getPostscript()
print "bitmap=", importanceFactorsRangeGraphThreshold.getBitmap()
