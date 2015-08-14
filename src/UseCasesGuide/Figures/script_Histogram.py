#! /usr/bin/python
# -*- coding: iso-8859-15 -*-

from openturns import *
from openturns.viewer import View

collection = HistogramPairCollection(3)
collection[0] = HistogramPair(1., 1.)
collection[1] = HistogramPair(4., 2.)
collection[2] = HistogramPair(2., 3.)
histogram = Histogram(0., collection)
histogram_pdf = histogram.drawPDF()
histogram_pdf.draw("pdf_Histogram")
#View(histogram_pdf).show()

histogram_cdf = histogram.drawCDF()
histogram_cdf.draw("cdf_Histogram")
#View(histogram_cdf).show()
