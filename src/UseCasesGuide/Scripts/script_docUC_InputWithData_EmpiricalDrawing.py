from __future__ import print_function
from openturns import *

# Create a scalar sample
N = 500
sample = Normal().getSample(N)
sample.setName('sample')

# Create a bidimensionnal sample
# For example  :
dist2D = ComposedDistribution([Normal(), Normal()], GumbelCopula(3))
dist2D.setDescription(['Marg1', 'Marg2'])
sample2 = dist2D.getSample(N)
sample2.setName('sample 2')
sample3 = dist2D.getSample(N)
sample3.setName('sample 3')

# BEGIN_TEX
###############################
# GRAPH 1 : Empirical CDF graph
###############################

# Generate the Graph structure for the empirical CDF graph
# graph range : min(sample) - 1, man(sample) + 1
# CARE : sample must be of dimension 1
sampleCDF = VisualTest.DrawEmpiricalCDF(
    sample, sample.getMin()[0] - 1.0, sample.getMax()[0] + 1.0)

# Or impose a bounding box : x-range and y-range
# boundingBox = [xmin, xmax, ymin, ymax]
myBoundingBox = [-5.0, 5.0, 0.0, 1.0]
sampleCDF.setBoundingBox(myBoundingBox)

# In order to see the graph without creating the associated files
# View(sampleCDF).show()

# Draw the graph on the file sampleCDF.png and sampleCDF.eps
# if the file adress is not fulfilled, the file is created in the current
# directory
sampleCDF.draw("sampleCDF")

###############################
# GRAPH 2 : Histogram graph with number of bars fixed by the user
###############################
# Generate the Graph structure for the histogram graph
# Number of bars fixed to 10
# CARE : sample must be of dimension 1
sampleHist = VisualTest.DrawHistogram(sample, 10)

# In order to visualize the graph
# View(sampleHist).show()

###############################
# GRAPH 3 : Histogram graph with free number of bars
###############################
# (automatically determined by OpenTURNS according to the Silverman rule)
# Generate the Graph structure for the histogram graph
# CARE : sample must be of dimension 1
sampleHistOpt = VisualTest.DrawHistogram(sample)

# In order to visualize the graph
# View(sampleHistOpt).show()

###############################
# GRAPH 4 : Superposition of two 2D samples where
###############################
# first sample is given as sample
# second sample is issued from a 2D distribution
# CARE : sample2 must be of dimension 2
# and dist is of dimension 2
# the sample issued from dist2D have the same size than sample2
cloudPdfGraph = VisualTest.DrawClouds(sample2, dist2D)
cloudPdfGraph.setLegendPosition('bottomright')

# In order to visualize the graph
# View(cloudPdfGraph).show()

###############################
# GRAPH 5 : Superposition of the two 2D samples : sample2 and sample3
###############################
# CARE : sample2 and sample3 must be of dimension 2
cloudPdfGraph2 = VisualTest.DrawClouds(sample2, sample3)
cloudPdfGraph2.setLegendPosition('bottomright')

# In order to visualize the graph
# View(cloudPdfGraph2).show()
# END_TEX
