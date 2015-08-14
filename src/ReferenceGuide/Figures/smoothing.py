#! /usr/bin/env python
from openturns import *

RandomGenerator.SetSeed(77)

# get a sample from a Normal distribution
normal = Normal(3.0, 1.0)
sample = normal.getSample(500)

# build an optimal smoothing  model
kernel_opt  = KernelSmoothing()
distrib_opt = kernel_opt.buildImplementation(sample)

# build an over smoothing model
h = distrib_opt.getBandwidth()[0];
kernel_over  = KernelSmoothing()
distrib_over = kernel_over.buildImplementation(sample, NumericalPoint(1, 3 * h))

# buils an under smoothing model
kernel_under  = KernelSmoothing()
distrib_under = kernel_under.buildImplementation(sample, NumericalPoint(1, h / 2.0))

# draw models PDF
distrib_opt.setName("Kernel estimate")
PDFGraph = distrib_opt.drawPDF()

drawable = PDFGraph.getDrawables()[0]
drawable.setColor("green")
drawable.setLineStyle("dashed")
PDFGraph = normal.drawPDF();
PDFGraph.add(drawable)
PDFGraph.setTitle("Non Parametric approach\n Optimal bandwidth")
PDFGraph.draw("OKsmoothing", 640, 480, GraphImplementation.PDF)


distrib_over.setName("Kernel estimate")
PDFGraph = distrib_over.drawPDF()
drawable = PDFGraph.getDrawables()[0]
drawable.setColor("green")
drawable.setLineStyle("dashed")
PDFGraph = normal.drawPDF();
PDFGraph.add(drawable)
PDFGraph.setTitle("Non Parametric approach\n Oversmoothing effect")
PDFGraph.draw("oversmoothing", 640, 480, GraphImplementation.PDF)

distrib_under.setName("Kernel estimate")
PDFGraph = distrib_under.drawPDF()
PDFGraph.setXTitle("x");
PDFGraph.setYTitle("y");

drawable = PDFGraph.getDrawables()[0]
drawable.setColor("green")
drawable.setLineStyle("dashed")
PDFGraph = normal.drawPDF();
PDFGraph.add(drawable)
PDFGraph.setTitle("Non Parametric approach\n Undersmoothing effect")
PDFGraph.draw("undersmoothing", 640, 480, GraphImplementation.PDF)
