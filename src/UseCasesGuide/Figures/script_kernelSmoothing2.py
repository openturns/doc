#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View

triang = Triangular(1.0, 2.0, 4.0)
norm = Normal(-1.0, 1.0)
norm2 = Normal(3.0, 1.0)
aCollection = DistributionCollection(3)
aCollection[0] = triang
aCollection[1] = norm
aCollection[2] = norm2
aCollection[0].setWeight(0.20)
aCollection[1].setWeight(0.50)
aCollection[2].setWeight(0.30)
myDistribution = Mixture(aCollection)


# Mixture
myDistribution_pdf = myDistribution.drawPDF(-4.0,8.0,150)
myDistribution_pdf_draw = myDistribution_pdf.getDrawable(0)
myDistribution_pdf_draw.setColor("black")
myDistribution_pdf_draw.setLegend("Real distribution")
myDistribution_pdf.setDrawable(myDistribution_pdf_draw,0)

myDistribution_pdf2 = Graph(myDistribution_pdf)

myDistribution_cdf = myDistribution.drawCDF(-4.0,8.0,150)
myDistribution_cdf_draw = myDistribution_cdf.getDrawable(0)
myDistribution_cdf_draw.setColor("black")
myDistribution_cdf_draw.setLegend("Real distribution")
myDistribution_cdf.setDrawable(myDistribution_cdf_draw,0)


#####################################
# Bandwith selection :   the 3 methods
#####################################

sample = myDistribution.getSample(1000)

# Normal kernel smoothing

kernel = KernelSmoothing()

# Silverman selection
myBandwithSilv = kernel.computeSilvermanBandwidth(sample)
gaussianSmoothedSilver = kernel.build(sample, myBandwithSilv)

gaussianSmoothedSilverPDF = gaussianSmoothedSilver.drawPDF(-4,8,251)
gaussianSmoothedSilverPDF_draw = gaussianSmoothedSilverPDF.getDrawables()[0]
gaussianSmoothedSilverPDF_draw.setColor("blue")
gaussianSmoothedSilverPDF_draw.setLegend("Silverman rule")
myDistribution_pdf.add(gaussianSmoothedSilverPDF_draw)

gaussianSmoothedSilverCDF = gaussianSmoothedSilver.drawCDF(-4,8,251)
gaussianSmoothedSilverCDF_draw = gaussianSmoothedSilverCDF.getDrawables()[0]
gaussianSmoothedSilverCDF_draw.setColor("blue")
gaussianSmoothedSilverCDF_draw.setLegend("Silverman rule")
myDistribution_cdf.add(gaussianSmoothedSilverCDF_draw)


# PLug-in selection selection
myBandwithPI = kernel.computePluginBandwidth(sample)
gaussianSmoothedPI = kernel.build(sample, myBandwithPI)

gaussianSmoothedPIPDF = gaussianSmoothedPI.drawPDF(-4,8,251)
gaussianSmoothedPIPDF_draw = gaussianSmoothedPIPDF.getDrawables()[0]
gaussianSmoothedPIPDF_draw.setColor("green")
gaussianSmoothedPIPDF_draw.setLegend("Plug-in Method")
myDistribution_pdf.add(gaussianSmoothedPIPDF_draw)

gaussianSmoothedPICDF = gaussianSmoothedPI.drawCDF(-4,8,251)
gaussianSmoothedPICDF_draw = gaussianSmoothedPICDF.getDrawables()[0]
gaussianSmoothedPICDF_draw.setColor("green")
gaussianSmoothedPICDF_draw.setLegend("Plug-in Method")
myDistribution_cdf.add(gaussianSmoothedPICDF_draw)



# Mixed selection selection
myBandwithMixed = kernel.computeMixedBandwidth(sample)
gaussianSmoothedMixed = kernel.build(sample, myBandwithMixed)

gaussianSmoothedMixedPDF = gaussianSmoothedMixed.drawPDF(-4,8,251)
gaussianSmoothedMixedPDF_draw = gaussianSmoothedMixedPDF.getDrawables()[0]
gaussianSmoothedMixedPDF_draw.setColor("red")
gaussianSmoothedMixedPDF_draw.setLegend("Mixed method")
myDistribution_pdf.add(gaussianSmoothedMixedPDF_draw)

gaussianSmoothedMixedCDF = gaussianSmoothedMixed.drawCDF(-4,8,251)
gaussianSmoothedMixedCDF_draw = gaussianSmoothedMixedCDF.getDrawables()[0]
gaussianSmoothedMixedCDF_draw.setColor("red")
gaussianSmoothedMixedCDF_draw.setLegend("Mixed method")
myDistribution_cdf.add(gaussianSmoothedMixedCDF_draw)



# Show the graph

myDistribution_pdf.setTitle("Effect of the bandwidth selection rules")
myDistribution_pdf.draw("kernelSmoothingBWSel_pdf")
#View(myDistribution_pdf).show()

myDistribution_cdf.setTitle("Effect of the bandwidth selection rules")
myDistribution_cdf.setLegendPosition("bottomright")
myDistribution_cdf.draw("kernelSmoothingBWSel_cdf")
#View(myDistribution_cdf).show()
