from __future__ import print_function
from openturns import *

# Time grid over which each process will be defined
N = 1024

# The choice of time grid size of form 2^ enables to perform
# and speed up the Fourier transform
myTimeGrid = RegularGrid(0.0, 1.0, N)

# Fix the second order model ==> parameters of the ExponentialCauchy model
amplitude = NumericalPoint([1, 1])
scale = NumericalPoint([1, 1])
myModel = ExponentialCauchy(amplitude, scale)

# Definition of the Normal process
# We define as well the temporal and spectral models
mySpectralProcess = SpectralNormalProcess(myModel, myTimeGrid)
myTemporalProcess = TemporalNormalProcess(myModel, myTimeGrid)


# BEGIN_TEX

# Get the covariance model in case of TemporalNormalProcess
myCovarianceModel = myTemporalProcess.getCovarianceModel()

# Compute the discretization of the covariance model on the time grid myTimeGrid
# The matrix is of size (nd) * (nd)
discretizedCovariance = myCovarianceModel.discretize(myTimeGrid)

# Get the sectral model in case of SpectralNormalProcess
mySpectralModel = mySpectralProcess.getSpectralModel()

# Compute the bilateral spectral density S at frequency f
# Get the first frequence
f = 3.0
bilateralSpectralDensity = mySpectralModel.computeSpectralDensity(f)

# END_TEX


# Spectral process realization draw
# As the model is of dimension 2, we plot the 2 marginals in the same graphSpectralCloud
# We add some labels to distinguish the marginals
graphSpectralRealization = Graph()
drawable0 = spectralRealization.drawMarginal(0).getDrawable(0)
drawable1 = spectralRealization.drawMarginal(1).getDrawable(0)
drawable0.setLegend('realization - marginal 1')
drawable0.setColor('blue')
drawable1.setLegend('realization - marginal 2')
drawable1.setColor('red')
graphSpectralRealization.add(drawable0)
graphSpectralRealization.add(drawable1)
graphSpectralRealization.setXTitle('Time')
graphSpectralRealization.setYTitle('Values')
graphSpectralRealization.setTitle("2D Spectral Normal process")
graphSpectralRealization.setLegendPosition('topright')
graphSpectralRealization.draw(
    "spectralNormal2D_realization", 800, 600, GraphImplementation.PNG)

# Temporal process realization draw
# we plot also the 2 marginals in the same graph and add some labels to
# distinguish the marginals
graphTemporalRealization = Graph()
drawable0 = temporalRealization.drawMarginal(0).getDrawable(0)
drawable1 = temporalRealization.drawMarginal(1).getDrawable(0)
drawable0.setLegend('realization - marginal 1')
drawable0.setColor('blue')
drawable1.setLegend('realization - marginal 2')
drawable1.setColor('red')
graphTemporalRealization.add(drawable0)
graphTemporalRealization.add(drawable1)
graphTemporalRealization.setXTitle('Time')
graphTemporalRealization.setYTitle('Values')
graphTemporalRealization.setTitle("2D Temporal Normal Process")
graphTemporalRealization.setLegendPosition('topright')
graphTemporalRealization.draw(
    "temporalNormal2D_realization", 800, 600, GraphImplementation.PNG)

# Spectral process realizations draw
# We draw only the first marginal
graphSpectralSample = spectralSample.drawMarginal(0)
graphSpectralSample.setTitle(
    str(N) + " realizations of the Normal process - First marginal")
for k in range(N):
    drawable = graphSpectralSample.getDrawable(k)
    drawable.setLegend('realization ' + str(k + 1))
    graphSpectralSample.setDrawable(drawable, k)

graphSpectralSample.draw(
    "spectralNormal2D_realizations", 800, 600, GraphImplementation.PNG)

# Temporal process sample draw ==> as for the spectral case, we draw the N
# realizationsof the first marginal
graphTemporalSample = temporalSample.drawMarginal(0)
graphTemporalSample.setTitle(
    str(N) + " realizations of the Normal process - First marginal")
for k in range(N):
    drawable = graphTemporalSample.getDrawable(k)
    drawable.setLegend('realization ' + str(k + 1))
    graphTemporalSample.setDrawable(drawable, k)

graphTemporalSample.draw(
    "temporalNormal2D_realizations", 800, 600, GraphImplementation.PNG)
