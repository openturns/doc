from __future__ import print_function
from openturns import *
from math import *

# Create the antecedent distribution (scalar)
myAntecedentDist = Normal()
# Create the mapping f
f = NumericalMathFunction('x', 'sin(x)+cos(x)')

# BEGIN_TEX

# Create the push-forward distribution
myDistribution = CompositeDistribution(f, myAntecedentDist)

# Use the simplified construction
myDistribution2 = myAntecedentDist.exp()

# Use chained operators
myDistribution3 = myAntecedentDist.abs().sqrt()

# END_TEX

graphPDF = myDistribution.drawPDF()
graphPDF.setTitle('Push-forward distribution - PDF')
graphPDF.setXTitle('x')
# Show(graphPDF)

graphPDF2 = myDistribution2.drawPDF()
graphPDF2.setTitle('Push-forward distribution - PDF')
graphPDF2.setXTitle('x')
# Show(graphPDF2)

graphPDF3 = myDistribution3.drawPDF()
graphPDF3.setTitle('Push-forward distribution - PDF')
graphPDF3.setXTitle('x')
# Show(graphPDF3)
