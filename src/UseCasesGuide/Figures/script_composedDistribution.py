from openturns import *
from openturns.viewer import View
from math import *


# Create a collection of distribution of dimension 3
aCollection = DistributionCollection(3)

# Create the first marginal : Weibul(mu, sigma, gamma) = Weibull(2.0, 1.0, 0.0)
weibDist = Weibull(2.0, 1.0, 0.0, Weibull.MUSIGMA)
weibDist.setName("First Marginal : Weibull")
aCollection[0] = weibDist

# Create the second marginal : Triangular(a,m,b) = Triangular(1.0, 3.0, 5.0)
triangularDist = Triangular(1.0, 3.0, 5.0)
triangularDist.setName("Second Marginal : Triangular")
aCollection[1] = triangularDist

# Create the third marginal : Uniform(a,b) = Uniform(2.0, 4.0)
uniformDist = Uniform(2.0, 4.0)
uniformDist.setName("Third Marginal : Uniform")
aCollection[2] = uniformDist

# Create a copula : Normal copula of dimension 3 fom Spearman rank correlation matrix
spearmanMatrix = CorrelationMatrix(3)
spearmanMatrix[0,1] = 0.25
spearmanMatrix[1,2] = 0.25
aCopula = NormalCopula(NormalCopula.GetCorrelationFromSpearmanCorrelation(spearmanMatrix))
aCopula.setName("Normal copula")

# Instanciate one distribution object
myDistribution = ComposedDistribution(aCollection, aCopula)

# Give a Description to the Distribution
aDescription = Description(3)
aDescription[0] = "X1 distribution"
aDescription[1] = "X2 distribution"
aDescription[2] = "X3 distribution"
myDistribution.setDescription(aDescription)

# Draw the PDF iso-curves of marginals 2-3
pointMin = NumericalPoint(2)
pointMin[0] = 1.0
pointMin[1] = 2.0
pointMax = NumericalPoint(2)
pointMax[0] = 5.0
pointMax[1] = 4.0
pointNumber = NumericalPoint(2)
pointNumber[0] = 101
pointNumber[1] = 101

marginal23_PDF = myDistribution.drawMarginal2DPDF(1,2, pointMin, pointMax, pointNumber)
marginal23_PDF.setTitle("Iso-PDF of marginals (2,3) of the 3D distribution")
marginal23_PDF.draw("ComposedDistribution_isoPDF_23", 800, 600, GraphImplementation.PNG)
marginal23_PDF.draw("ComposedDistribution_isoPDF_23", 800, 600, GraphImplementation.PDF)
#View(marginal23_PDF).show()


# Draw the PDF iso-curves of marginals 1-2
pointMin[0] = 0.0
pointMin[1] = 1.0
pointMax[0] = 6.1
pointMax[1] = 5.0

marginal12_PDF = myDistribution.drawMarginal2DPDF(0,1, pointMin, pointMax, pointNumber)
marginal12_PDF.setTitle("Iso-PDF of marginals (1,2) of the 3D distribution")
marginal12_PDF.draw("ComposedDistribution_isoPDF_12")
marginal12_PDF.draw("ComposedDistribution_isoPDF_12", 800, 600, GraphImplementation.PNG)
marginal12_PDF.draw("ComposedDistribution_isoPDF_12", 800, 600, GraphImplementation.PDF)
#View(marginal12_PDF).show()


# Draw the PDF iso-curves of marginals 1-3
pointMin[0] = 0.0
pointMin[1] = 2.0
pointMax[0] = 6.1
pointMax[1] = 4.0

marginal13_PDF = myDistribution.drawMarginal2DPDF(0,2, pointMin, pointMax, pointNumber)
marginal13_PDF.setTitle("Iso-PDF of marginals (1,3) of the 3D distribution")
marginal13_PDF.draw("ComposedDistribution_isoPDF_13", 800, 600, GraphImplementation.PNG)
marginal13_PDF.draw("ComposedDistribution_isoPDF_13", 800, 600, GraphImplementation.PDF)
#View(marginal13_PDF).show()


# Distribution of dimension 2
dist_2 = ComposedDistribution([Normal(), Triangular(0.0, 2.0, 3.0)], ClaytonCopula(2.3))

dist_1 = Normal()

qMin=0.1
qMax=0.9
nbrPoints=101

quantileGraph=dist_2.drawQuantile(qMin,qMax, nbrPoints) 
quantileGraph.setXTitle('Margin 1')
quantileGraph.setYTitle('Margin 2')
quantileGraph.setTitle('Quantile Curve')
quantileGraph.draw('QuantileCurve', 800, 600, GraphImplementation.PNG)

quantileGraph=dist_1.drawQuantile(qMin,qMax, nbrPoints) 
quantileGraph.setYTitle('Quantile')
quantileGraph.setXTitle('Order')
quantileGraph.setTitle('Quantile Curve')
quantileGraph.draw('QuantileCurve2', 800, 600, GraphImplementation.PNG)


