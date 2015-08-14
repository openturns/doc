from openturns import *

# Create the antecedent distribution (scalar)
myAntecedentDist = Normal()
# Create the mapping f
f = NumericalMathFunction('x', 'sin(x)+cos(x)')

# Create the image distribution
myDistribution = CompositeDistribution(f, myAntecedentDist)
# Use the simplified construction
myDistribution2 = myAntecedentDist.exp()
# Use chained operators
myDistribution3 = myAntecedentDist.abs().sqrt()

graphPDF = myDistribution.drawPDF()
graphPDF.setTitle('Push-forward distribution - PDF')
graphPDF.setXTitle('x')
graphPDF.draw('ImageDist', 800, 600, GraphImplementation.PNG)
#Show(graphPDF)

graphPDF2 = myDistribution2.drawPDF()
graphPDF2.setTitle('Push-forward distribution - PDF')
graphPDF2.setXTitle('x')
graphPDF2.draw('ImageDist2', 800, 600, GraphImplementation.PNG)
#Show(graphPDF2)

graphPDF3 = myDistribution3.drawPDF()
graphPDF3.setTitle('Push-forward distribution - PDF')
graphPDF3.setXTitle('x')
graphPDF3.draw('ImageDist3', 800, 600, GraphImplementation.PNG)
#Show(graphPDF3)


