from openturns import *



# KendallPlot tests

# Case 1 : Test of a copula to a sample

# Create the sample
size = 100
copula = FrankCopula(1.5)
copula2 = GumbelCopula(4.5)

sample1 = copula.getSample(size)
sample1.setName("data 1")

# The test says ok
kendallPlot1 = VisualTest.DrawKendallPlot(sample1, copula)
kendallPlot1.setTitle('Kendall Plot : data vs Frank copula')
#View(kendallPlot1).show()
kendallPlot1.draw("KendallPlotCopula", 800, 600, GraphImplementation.PNG)
kendallPlot1.draw("KendallPlotCopula", 800, 600, GraphImplementation.PDF)


# The test says no
kendallPlot2 = VisualTest.DrawKendallPlot(sample1, copula2)
kendallPlot2.setTitle('Kendall Plot : data vs Gumbel copula')
#View(kendallPlot2).show()
kendallPlot2.draw("KendallPlotCopulaBad", 800, 600, GraphImplementation.PNG)
kendallPlot2.draw("KendallPlotCopulaBad", 800, 600, GraphImplementation.PDF)



# Case 2 : Test whether two samples have the same copula

sample2 = copula.getSample(size)
sample2.setName("data 2")
sample3 = copula2.getSample(size)
sample3.setName("data 3")


# The test says ok
kendallPlot3 = VisualTest.DrawKendallPlot(sample2, sample1)
kendallPlot3.setTitle('Kendall Plot : data 1 vs data 2')
#View(kendallPlot3).show()
kendallPlot3.draw("KendallPlotSample", 800, 600, GraphImplementation.PNG)
kendallPlot3.draw("KendallPlotSample", 800, 600, GraphImplementation.PDF)

# The test says no
kendallPlot4 = VisualTest.DrawKendallPlot(sample3, sample1)
kendallPlot4.setTitle('Kendall Plot : data 1 vs data 3')
#View(kendallPlot4).show()
kendallPlot4.draw("KendallPlotSampleBad", 800, 600, GraphImplementation.PNG)
kendallPlot4.draw("KendallPlotSampleBad", 800, 600, GraphImplementation.PDF)
