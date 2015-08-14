from openturns import *


# dimension of the model
dimension = 1

# Time grid over which all the processes will be defined
N = 100

# Fix the timeGrid over which the process is evaluated
timeGrid = RegularGrid(0.0,1.0, N)


# Strong independent bidimensional normal white noise
epsilon = 0.01
noiseDistribution = Normal(0.0, epsilon)
whiteNoise = WhiteNoise(noiseDistribution, timeGrid)

# AR(4) definition
p = 4
arCoefficients = ARMACoefficients(NumericalPoint([0.4,0.3,0.2,0.1]))

# the proces is AR(4) ==> q = 0
q = 0
maCoefficients = ARMACoefficients(q, dimension)

# We build the ARMA proces
armaProcess = ARMA(arCoefficients, maCoefficients, whiteNoise)


# 1 realization of the process is done ==> the first call migh be cpu consuming (computation of thermalization parameter)
realization = armaProcess.getRealization()
# Draw the realization of the ARMA
graph = realization.drawMarginal(0)
drawable = graph.getDrawable(0)
drawable.setLegendName('realization')
graph.setDrawable(drawable, 0)
graph.setTitle("ARMA("+str(p)+','+str(q)+") realization")
graph.draw("arma1D_realization", 800, 600, GraphImplementation.PNG)
graph.draw("arma1D_realization", 800, 600, GraphImplementation.PDF)

# The state is fixed (just after the realization)
# we get one futur realization of the AR process on the 50 next instants
prediction = armaProcess.getFuture(50)

# We draw the futre of the graph
graph = prediction.drawMarginal(0)
drawable = graph.getDrawable(0)
drawable.setLegendName('prediction')
graph.setDrawable(drawable, 0)

graph.setTitle("Prediction of the ARMA process")
graph.draw("arma1D_prediction", 800, 600, GraphImplementation.PNG)
graph.draw("arma1D_prediction", 800, 600, GraphImplementation.PDF)

# We get now 5 futur realizations
predictions = armaProcess.getFuture(50, 5)

# We draw all the futurs on the same graph
graph = predictions.drawMarginal(0)
graph.setTitle("5 predictions of the ARMA process")
for k in range(5):
  drawable = graph.getDrawable(k)
  drawable.setLegendName('prediction ' + str(k+1))
  graph.setDrawable(drawable, k)

graph.draw("arma1D_predictions", 800, 600, GraphImplementation.PNG)
graph.draw("arma1D_predictions", 800, 600, GraphImplementation.PDF)


# We want to get a ProcessSample of size 5
# This is done here using the getSample method
# We draw then the values on the same graph
sample = armaProcess.getSample(5)
graph = sample.drawMarginal(0)
graph.setTitle("5 realizations of the ARMA process")
for k in range(5):
  drawable = graph.getDrawable(k)
  drawable.setLegendName('realization ' + str(k+1))
  graph.setDrawable(drawable, k)

graph.draw("arma1D_realizations", 800, 600, GraphImplementation.PNG)
graph.draw("arma1D_realizations", 800, 600, GraphImplementation.PDF)
