from __future__ import print_function
from openturns import *

# Distribution of dimension 1
dist_1 = Normal()
dist_1.setName("dist1")

# Distribution of dimension 2
dist_2 = ComposedDistribution(
    [Normal(), Triangular(0.0, 2.0, 3.0)], ClaytonCopula(2.3))
dist_2.setName('dist2')


# Distribution of dimension 3
# create a copula of dimension 3
# from the Student distribution of distribution 3
copula_dim3 = Student(5.0, 3).getCopula()
dist_3 = ComposedDistribution(
    [Normal(), Triangular(0.0, 2.0, 3.0), Exponential(0.2)], copula_dim3)
dist_3.setName("dist3")

# BEGIN_TEX
# Get the dimension fo the distribution
dim = dist_2.getDimension()
print("Dimension of the distribution = ", dim)

# Get one marginal distribution
# Care : the numerotation begins at 0
marginal_2 = dist_2.getMarginal(1)

# The marginal distribution of several components
# Put the indices of the concerned components together
# for example, the two first components of dist_3
marginal_12 = dist_3.getMarginal((0, 1))

# Get the copula
copula = dist_2.getCopula()

# Ask some properties on the copula
print("hasIndependentCopula ? ", dist_2.hasIndependentCopula())
print("hasEllipticalCopula ? ", dist_2.hasEllipticalCopula())

# Get the mean vector of the distribution
meanVector = dist_2.getMean()

# Get the covariance matrix of the distribution
meanVector = dist_2.getCovariance()

# Get the kurtosis vector of the distribution
kurtosisVector = dist_2.getKurtosis()

# Get the standard deviation vector of the distribution
standardDeviationVector = dist_2.getStandardDeviation()

# Get the skewness vector of the distribution
skewnessVector = dist_2.getSkewness()

# Get one realization of the distribution
oneRealisationVector = dist_2.getRealization()

# Get several realizations of the distribution
# For example, 100 ones
OneHundred_realizations = dist_2.getSample(100)

# Evaluate the CDF and PDF
# For example, at the mean point
dist_2.computeCDF(dist_2.getMean())
dist_2.computePDF(dist_2.getMean())
dist_2.computeComplementaryCDF(dist_2.getMean())


# For the evaluation on a NumericalSample
dist_2.computeCDF(dist_2.getSample(10))
dist_2.computePDF(dist_2.getSample(10))

# Evaluate the probability content of an interval
# in dimension 1
interval = Interval(-2.0, 3.0)
probability = dist_1.computeProbability(interval)

# in dimension 2 : [xmin, ymin], [ymin, ymax]
interval = Interval([1.2, -1], [3.4, 2])
probability = dist_2.computeProbability(interval)

# Evaluate the quantile of order p
# For example, the quantile 90%
quantile_Vector_90 = dist_2.computeQuantile(0.90)
# and the quantile of order 1-p
quantile_Vector_10 = dist_2.computeQuantile(0.90, True)

# Evaluate the quantiles of order p et q
# For example, the quantile 90% and 95%
quantile_List = dist_1.computeQuantile([0.90, 0.95])
# and the quantile of order 1-p and 1-q
compQuantile_List = dist_1.computeQuantile([0.90, 0.95], True)


# Evaluate the characteristic function of the distribution at pointVector
# Only for dimension 1
complexResult = dist_1.computeCharacteristicFunction(dist_1.getMean()[0])

# Evaluate the derivatives of the PDF/CDF with respect to the parameters at a particular point
# For example, with dimension 2, at the mean point
derivatives_PDF_Vector = dist_2.computePDFGradient(dist_2.getMean())
derivatives_CDF_Vector = dist_2.computeCDFGradient(dist_2.getMean())


#####################################
# GRAPH 1 : Draw the PDF (CDF)
# for a distribution of dimension 1
#####################################

# No specification of support
PDF_1D_graph = dist_1.drawPDF()
# Or on [-3, 3]
PDF_1D_graph = dist_1.drawPDF(-3., 3.)

# Or impose a bounding box : x-range and y-range
# boundingBox = [xmin, xmax, ymin, ymax]
myBoundingBox = NumericalPoint((-3., 3., 0, 0.5))
PDF_1D_graph.setBoundingBox(myBoundingBox)

# In order to see the graph without creating the associated files
# View(PDF_1D_graph).show()

# Create the files corresponding to the graph
# the files .EPS, .PNG and .FIG are created in the current python session
PDF_1D_graph.draw("PDF_graph")

# Or only the .EPS file
# 640 and 480 are the pixels number in both axes
PDF_1D_graph.draw("PDF_graph", 640, 480, GraphImplementation.EPS)


#####################################
# GRAPH 2 : Draw the PDF (CDF) iso-curves
# for a distribution of dimension 2
#####################################

# No specification of support
PDF_graph = dist_2.drawPDF()

# Or Specify the support pointMin and pointMax
# the graph will be drawn in the box with
# low-left corner : pointMin= (xmin, ymin)
# and up-right corner : pointMax = (xmax, ymax)
pointMin = NumericalPoint((-3., 0.0))
pointMax = NumericalPoint((3., 3.5))

# Specify the point number in each direction (curve look)
pointNumber = Indices((201, 201))

PDF_graph = dist_2.drawPDF(pointMin, pointMax, pointNumber)

# To impose a bounding box : see Graph 1

# Change the default levels where the contours are drawn
# Define the levels for example
nlev = 31
levels = NumericalPoint(nlev)
for i in range(nlev):
    levels[i] = 0.25 * nlev / (1.0 + i)
    # Change them in the contour drawable
    PDF_graph_contour = PDF_graph.getDrawable(0)
    PDF_graph_contour.setLevels(levels)
    # If you don't need the labels on the iso curves
    PDF_graph_contour.setDrawLabels(False)

PDF_graph.setDrawable(PDF_graph_contour, 0)

# To visualize the graph : see Graph 1


#####################################
# GRAPH 3 : Draw the PDF (CDF)
# of the 1D marginals for a distribution of dimension >=2
#####################################

# For example, marginal 1
# Care : the numerotation begins at 0
PDF_graph = dist_3.drawMarginal1DPDF(1, -5.0, 5.0, 101)

# To specify the support  : see Graph 1
# To impose a bounding box : see Graph 1

# To visualize the graph : see Graph 1


#####################################
# GRAPH 4 : Draw the PDF (CDF)
# iso-curves for a distribution of dimension n>2
#####################################

# For example, the marginals i and j
# Care : the numerotation begins at 0

# Specify the support pointMin = (xmin, ymin)
# and  pointMax = (xmax, ymax)
# and the number of points of the curve (all vectors)
pointMin = NumericalPoint((-3., 0.0))
pointMax = NumericalPoint((3., 3.5))
pointNumber = Indices((101, 101))
PDF_graph = dist_3.drawMarginal2DPDF(0, 1, pointMin, pointMax, pointNumber)

# To specify the support  : see Graph 1

# To impose a bounding box : see Graph 1

#  To Change the default levels where
# the contours are drawn : see Graph 2


#####################################
# GRAPH 4 : Draw the quantile curve
#####################################

# Define the range and the number of points
qMin = 0.2
qMax = 0.6
nbrPoints = 101
quantileGraph = dist_2.drawQuantile(qMin, qMax, nbrPoints)

# END_TEX
quantileGraph.setXTitle('Margin 1')
quantileGraph.setYTitle('Margin 2')
quantileGraph.setTitle('Quantile Curve')
# Show(quantileGraph)
