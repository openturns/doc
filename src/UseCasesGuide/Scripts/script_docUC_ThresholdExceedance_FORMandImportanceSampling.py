from __future__ import print_function
from openturns import *

# Create the model Y = x1^2 + 2*x2
model = NumericalMathFunction(["x1", "x2"], ["y"], ["x1^2+2*x2"])

# Create the input distribution and random vector X
inputDist = ComposedDistribution([Normal(), Normal()], IndependentCopula(2))
inputDist.setDescription(['X1', 'X2'])

inputVector = RandomVector(inputDist)

# Create the output random vector Y=model(X)
output = RandomVector(model, inputVector)

# To have a beautifull graph of importance factors,
# give the output random variable a name
output.setName("MyOutputY")

# Create the event Y > 4
threshold = 4
myEvent = Event(output, Greater(), threshold)

# Create a NearestPoint algorithm with the Cobyla algorithm
myCobyla = Cobyla()

# Create a FORM algorithm
myStartingPoint = inputDist.getMean()
myAlgoFORM = FORM(myCobyla, myEvent, myStartingPoint)

# Run the algorithm and take the result
myAlgoFORM.run()
myAnalyticalResult = myAlgoFORM.getResult()

# BEGIN_TEX
# Create the post analytical importance sampling simulation algorithm
myPostAnalyticalISAlgo = PostAnalyticalImportanceSampling(myAnalyticalResult)
myPostAnalyticalISAlgo.run()
print('myPostAnalyticalISAlgo - Results = ',
      myPostAnalyticalISAlgo.getResult())

# Create the post analytical controlled importance sampling simulation
# algorithm
myPostAnalyticalControlledISAlgo = PostAnalyticalControlledImportanceSampling(
    myAnalyticalResult)
myPostAnalyticalControlledISAlgo.run()
print('myPostAnalyticalControlledISAlgo - Results = ',
      myPostAnalyticalControlledISAlgo.getResult())
# END_TEX
