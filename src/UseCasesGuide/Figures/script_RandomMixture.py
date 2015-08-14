from openturns import *

# X1 : Exponential(1.5)
X1 = Exponential(1.5)


# X2 : Normal(4,1)
X2 = Normal(4,1)



# Put them in a DistributionCollection
distribList = DistributionCollection(2)
distribList[0] = X1
distribList[1] = X2


# Create the constant coefficient a0
a0 = 2.0

# Create the numerical of the distribution weights
# coefficients a1, a2
weight = NumericalPoint(2)
weight[0] = 5
weight[1] = 1

# Create the Random Mixture
myRandomMixtureY = RandomMixture(distribList, weight, a0)

# Ask myRandomMixtureY to draw its pdf
pdfY = myRandomMixtureY.drawPDF()

# Save it in a file at format .FIG, .EPS anf .PNG
pdfY.draw("RandomMixture_pdf")

# Visualize the graph without saving it
#View(pdfY).show()

# Idem on CDF
cdfY = myRandomMixtureY.drawCDF()
cdfY.draw("RandomMixture_cdf")

#View(cdfY).show()
