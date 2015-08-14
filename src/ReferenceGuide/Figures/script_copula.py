from openturns import *
from openturns.viewer import ViewImage
from math import *

numCop = 8
collCop = CopulaCollection(numCop)
descCop = Description(numCop)
scaling = NumericalPoint(numCop)
nlevels = UnsignedLongCollection(numCop)

# Graph 1 : Normal copula

R = CorrelationMatrix(2)
R[0,1] = 0.8
collCop[0] = Copula(NormalCopula(R))
descCop[0] = "Normal copula, rho=0.8"

# Graph 2 : Frank copula
theta = 9.2
collCop[1] = Copula(FrankCopula(theta))
descCop[1] = "Frank copula, theta=9.2"

## Graph 3 : Gumbel copula
theta = 2.5
collCop[2] = Copula(GumbelCopula(theta))
descCop[2] = "Gumbel copula, theta=2.5"

## Graph 4 : Clayton copula
theta = 2.5
collCop[3] = Copula(ClaytonCopula(theta))
descCop[3] = "Clayton copula, theta=2.5"

## Graph 5 : Independent Copula
collCop[4] = Copula(IndependentCopula(2))
descCop[4] = "Independent copula"

## Graph 6 : FarlieGumbelMorgenstern Copula
collCop[5] = Copula(FarlieGumbelMorgensternCopula(0.7))
descCop[5] = "FGM copula"

## Graph 7 : AliMikhailHaq Copula
collCop[6] = AliMikhailHaqCopula((0.7))
descCop[6] = "AMH copula"


## Graph 8 : Sklar Copula
myStudent = Student(3.0, NumericalPoint(2, 1.0), NumericalPoint(2, 3.0), CorrelationMatrix(2))
collCop[7] =  SklarCopula(Distribution(myStudent))
descCop[7] = "Sklar copula from a Student(2)"



# Draw the iso curve

xMin = NumericalPoint(2)
xMin[0] = 0.0
xMin[1] = 0.0
xMax = NumericalPoint(2)
xMax[0] = 1.0
xMax[1] = 1.0
pointNumber = NumericalPoint(2)
pointNumber[0] = 301
pointNumber[1] = 301


for indCop in range(collCop.getSize()):
    copula_isoPDF = collCop[indCop].drawPDF()
    contourCopula = copula_isoPDF.getDrawable(0)
    copula_isoPDF.setDrawable(contourCopula, 0)
    copula_isoPDF.setTitle(descCop[indCop])
    copula_isoPDF.setLegendPosition("bottomright")
    boundingBox = copula_isoPDF.getBoundingBox()
    Lx = boundingBox[1] - boundingBox[0]
    boundingBox[0] = boundingBox[0]-0.2*Lx
    boundingBox[1] = boundingBox[1]+0.2*Lx
    copula_isoPDF.setBoundingBox(boundingBox)
    copula_isoPDF.draw(collCop[indCop].getName(), 800,600)
    Show(copula_isoPDF)
