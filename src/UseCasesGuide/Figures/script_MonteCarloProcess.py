from openturns import *

# dimension
dimension = 2

# Creation of a white noise process
myStartTime = 0.0
myTimeStep = 0.1
mySteps = 10
myTimeGrid = RegularGrid(myStartTime, myTimeStep, mySteps)

# Create a collection of distribution
# The collection is composed of standard gaussian
myDistribution = Normal()
myCollection = DistributionCollection(dimension, myDistribution)

# Finally get the composed distribution
myComposedDistribution = ComposedDistribution(myCollection)

# The white noise is ready
myWhiteNoise = WhiteNoise(Distribution(myComposedDistribution), myTimeGrid)
myProcess = Process(myWhiteNoise)

# Definition of the domain
# The domain is [1, 2] x [1, 2]
myDomain = Interval(NumericalPoint(dimension, 1.0), NumericalPoint(dimension, 2.0))

myEvent = EventProcess(myProcess, Domain(myDomain))

# We are interested in the event : process visits the domain
# We create an event using a domain and a process
myEvent = Event(myProcess, myDomain)

# size of simulations : 100 * 1000 simulations
# Monte-Carlo algorithm
size = 1000
blocksize = 100
cv = 0.0001 # coeff of variations
myMonteCarloAlgo = MonteCarlo(myEvent)
myMonteCarloAlgo.setMaximumOuterSampling(size)
myMonteCarloAlgo.setBlockSize(blocksize)
myMonteCarloAlgo.setMaximumCoefficientOfVariation(cv)
myMonteCarloAlgo.run()

result = myMonteCarloAlgo.getResult()
graph = myMonteCarloAlgo.drawProbabilityConvergence(0.95)

graph.draw("MonteCarloEventProcessConvergency", 800, 600, GraphImplementation.PNG)
graph.draw("MonteCarloEventProcessConvergency", 800, 600, GraphImplementation.PDF)
