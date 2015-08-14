from __future__ import print_function
from openturns import *

# Generate a sample
# here a scalar one
dist = Mixture([Normal(2.0, 1.0), Normal(5.0, 1.0)])
dist.setName('real dist')
sample = dist.getSample(1000)
sample.setName('My sample')

# BEGIN_TEX
##################################
# STEP 1 : Creation of the kernel

# Create the default kernel : kernel product of N(0.0, 1.0)
kernel = KernelSmoothing()

# Create a specified kernel
# for example, a Uniform one with default parameters
kernel2 = KernelSmoothing(Uniform())

# Specify totally the kernel
# CARE : the kernel smoothing is more efficient
# when the kernel support is symmetric qith respect to 0
kernel3 = KernelSmoothing(Triangular(-2.0, 0.0, 2.0))


#####################################################
# STEP 2 : Creation of the kernel smoothed distribution
# The dimension of the distribution is authomatically
# detected from the numerical sample

# With no bandwidth specification : the method employed is
# adapted to the size of the numerical sample
# with no boudary treatment
kernelSmoothedDist = kernel.build(sample)

# Add a boundary treatment in dimension 1 only
kernelSmoothedDist2 = kernel.build(sample, True)

# Check the bandwidth used
print("kernel bandwidth=", kernel.getBandwidth())

# Specify a particular bandwidth evaluated
# according to the Silverman rule
myBandwith = kernel.computeSilvermanBandwidth(sample)

# or according to the plug-in method
# applied in the entire numerical sample
myBandwith2 = kernel.computePluginBandwidth(sample)

# or according to the mixted plug-in method
myBandwith3 = kernel.computeMixedBandwidth(sample)

# Then build the estimation with the specified bandwidth
kernelSmoothedDist = kernel.build(sample, myBandwith)


############################################
# GRAPH : In dimension 1, superposition of the kernel smoothed CDF
# and the empirical CDF
############################################
# Create the graph containing the kernel smoothed CDF
kernelSmoothedCDF = kernelSmoothedDist.drawCDF()

# Draw the empirical CDF of the sample on the same graph
empiricalCDF = VisualTest.DrawEmpiricalCDF(
    sample, sample.getMin()[0], sample.getMax()[0])
drawableEmpiricalCDF = empiricalCDF.getDrawable(0)
drawableEmpiricalCDF.setColor('blue')

# Add the second drawable on the first graph
kernelSmoothedCDF.add(drawableEmpiricalCDF)

# To visualize the graph
# View(kernelSmoothedCDF).show()

# Draw the final graph on the file smoothedCDF-EmpiricalCDF at format .eps, .png and .fig
# if the adress is not fulfilled, the file is created in the current directory
kernelSmoothedCDF.draw("smoothedCDF-EmpiricalCDF")

# END_TEX
