from openturns import *
myTimeGrid=RegularGrid(0,0.1, 101)

# Define a scalar temporal normal process on the mesh
amplitude=[1.0]
scale=[0.2]
myCovModel=ExponentialModel(amplitude,scale)

myProcess=TemporalNormalProcess(myCovModel, myTimeGrid)

myField=myProcess.getRealization()

myGraph1=myField.drawMarginal(0, False)
myGraph1.setTitle('Time series with no interpolation')
Show(myGraph1)
myGraph1.draw('timeSeriesNoInterp', 800, 400, GraphImplementation.PNG)

myGraph2=myField.drawMarginal(0)
myGraph2.setTitle('Time series with linear interpolation')
Show(myGraph2)
myGraph2.draw('timeSeriesInterp', 800, 400, GraphImplementation.PNG)
