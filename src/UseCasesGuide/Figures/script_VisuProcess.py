from openturns import *
from math import *

# Creation of a mesh of dimension 1
tMin = 0.0
tMax = 1.0
n=21
tStep=(tMax-tMin)/n
myMesh= RegularGrid(tMin, tStep, n)

############################"
# Case 1

# Creation of a functional basis process
# of dimension 1
# basis
imax=10
myFuncColl=NumericalMathFunctionCollection(0)
myCoeff=DistributionCollection(0)
for i in range(1,imax+1):
    myFuncColl.add(NumericalMathFunction('x', 'cos(' + str(2*i*pi) + '*x)'))
    myCoeff.add(Normal(0, 1.0/i))
    myCoeffDistribution=ComposedDistribution(myCoeff)
    myBasis=Basis(myFuncColl)
    myFuncBasProc= FunctionalBasisProcess(myCoeffDistribution, myBasis, myMesh)

# Get one realization
RandomGenerator.SetSeed(0)
myField=myFuncBasProc.getRealization()
myGraph1= myField.drawMarginal()

# Get one continuous realization
RandomGenerator.SetSeed(0)
myFunc=myFuncBasProc.getContinuousRealization()
myGraph2=myFunc.draw(tMin, tMax)
myGraph2.add(myGraph1)
myGraph2.setColors(['red', 'blue'])
myGraph2.setLegends(['real', 'continuous real'])
myGraph2.setLegendPosition('bottomright')
# myGraph2=myFunc.draw(myMesh.getVertices().getMin(), myMesh.getVertices().getMax())
myGraph2.setTitle('Realization versus Continuous Realization')
myGraph2.setYTitle('y')
#Show(myGraph2)
#myGraph2.draw('FuncBasProc_real', 800, 600, GraphImplementation.PNG)

################
# Case 2

# Creation of the scalar temporal normal process
amplitude=[1.0]
scale=[4.0]
myCovarianceModel = ExponentialModel(amplitude, scale)
myTNP=TemporalNormalProcess(myCovarianceModel, myMesh)

# Get one realization
RandomGenerator.SetSeed(0)
myField=myTNP.getRealization()
myGraph3= myField.drawMarginal()

# to refuse the interpolation:
# myGraph3= myField.drawMarginal(0, False)

# Get one continuous realization
RandomGenerator.SetSeed(0)
myFunc=myTNP.getContinuousRealization()
myGraph4=myFunc.draw(tMin, tMax, 1024)
myGraph4.add(myGraph3)
myGraph4.setColors(['red', 'blue'])
myGraph4.setLegends(['real', 'continuous real'])
myGraph4.setLegendPosition('bottomleft')
# myGraph4=myFunc.draw(myMesh.getVertices().getMin(), myMesh.getVertices().getMax())
myGraph4.setTitle('Realization versus Continuous Realization')
myGraph4.setYTitle('y')
Show(myGraph4)
#myGraph4.draw('TNProc_real', 800, 600, GraphImplementation.PNG)
