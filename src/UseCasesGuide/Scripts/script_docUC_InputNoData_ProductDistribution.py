from __future__ import print_function
from openturns import *
from math import *

# Create the left distribution
distX = Uniform(0.1, 1.0)

# Create the right distribution
distY = Uniform(2.0, 3.0)

# BEGIN_TEX

# Create the product distribution
distZ = ProductDistribution(distX, distY)

# Get the left distribution
leftDist = distZ.getLeft()

# Get the right distribution
rightDist = distZ.getRight()

# END_TEX

graphPDF = distZ.drawPDF(0.0, 4.0)
graphPDF.setTitle('Product distribution - PDF')
graphPDF.setXTitle('z')
graphPDF.setLegendPosition('')
# Show(graphPDF)
