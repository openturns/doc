from openturns import *


# Dimension parameter
dimension = 1

# Amplitude and scale values of the Exponential model
amplitude = NumericalPoint(dimension, 1.0)
scale = NumericalPoint(dimension, 1.0)

# Size of the TimeGrid
size = 20
dt = 0.1
timeGrid = RegularGrid(0., dt, size)

# Exponential covariance model
model = ExponentialCauchy(amplitude, scale)
myProcess = TemporalNormalProcess(model, timeGrid)

# Create a sample of size N
N = 10000
sample = myProcess.getSample(N)

# NonStationaryCovarianceModelFactory using default parameter
myFactory = NonStationaryCovarianceModelFactory()

# Build a UserDefinedCovarianceModel
myCovarianceModel = myFactory.build(sample)

# Graph
myGraph = Graph('Covariance estimation', 'time', 'Covariance value C(t,s) for t=0', True)
sampleT = NumericalSample(size, 1)
sampleValueEstimated = NumericalSample(size, 1)
sampleValueModel = NumericalSample(size, 1)
for i in range(size):
    t = timeGrid.getValue(i)
    sampleT[i, 0] = t
    for j in range(size):
        s = timeGrid.getValue(j)
        estimatedValue = myCovarianceModel.computeCovariance(t,s)
        modelValue = model.computeCovariance(t,s)
        if (i == 0):
            sampleValueEstimated[j, 0] = estimatedValue[0,0]
            sampleValueModel[j, 0] = modelValue[0,0]
            print  "Covariance C(" , t , ", " , s , ")\n", " evaluation = \n" , estimatedValue , " model = \n" , modelValue

# Drawing...
myCurveEstimated = Curve(sampleT, sampleValueEstimated, 'Estimated model')
myGraph.add(myCurveEstimated)
myCurveModel = Curve(sampleT, sampleValueModel, 'Exact model')
myCurveModel.setColor('red')
myGraph.add(myCurveModel)
myGraph.setLegendPosition('topright')
myGraph.draw('NonStationaryCovarianceModelEstimation', 800, 600,  GraphImplementation.PNG)
myGraph.draw('NonStationaryCovarianceModelEstimation', 800, 600,  GraphImplementation.PDF)
