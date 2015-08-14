from openturns import *
from math import *

# Create the left distribution
distX = Uniform(0.1, 1.0)

# Create the right distribution
distY = Uniform(2.0, 3.0)

# Create the product distribution
distZ = ProductDistribution(distX, distY)

# Display the pdf
graphPDF = distZ.drawPDF(0.0, 4.0)
graphPDF.setTitle('Product distribution - PDF')
graphPDF.setXTitle('z')
graphPDF.setLegendPosition('')

graphPDF.draw('productDist', 800, 600, GraphImplementation.PNG)



