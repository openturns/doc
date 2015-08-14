from __future__ import print_function
from openturns import *

myEntireDist = Student(2.5)

# Define the bounds
myLowerBound = -2.0
myUpperBound = 3.5

# BEGIN_TEX
#####################################
# CASE 1 : Truncate the distribution
# within the range [myLowerBound, myUpperBound]
#####################################

myTruncatedDistribution = TruncatedDistribution(
    myEntireDist, myLowerBound, myUpperBound)

# See the result on the PDF
myTruncatedDistribution.setName('my truncated dist')
# View(myTruncatedDistribution.drawPDF()).show()


#####################################
# CASE 2 : Truncate the distribution
# within the range $[myLowerBound, \infty[$ or [myLowerBound, max[
# if myEntireDistribution was already bounded by $max$
#####################################

myTruncatedDistribution = TruncatedDistribution(
    myEntireDist, myLowerBound, TruncatedDistribution.LOWER)

# See the result on the PDF
myTruncatedDistribution.setName('my truncated dist')
# View(myTruncatedDistribution.drawPDF()).show()

#####################################
# CASE 3 : Truncate the distribution
# within the range [-\infty, myUpperBound[ or [min, myUpperBound[
# if myEntireDistribution was already bounded by $min$
#####################################

myTruncatedDistribution = TruncatedDistribution(
    myEntireDist, myUpperBound, TruncatedDistribution.UPPER)

# See the result on the PDF
myTruncatedDistribution.setName('my truncated dist')
# View(myTruncatedDistribution.drawPDF()).show()


# Recuperate the initial distribution
initialDistribution = myTruncatedDistribution.getDistribution()
# View(initialDistribution.drawPDF()).show()
# END_TEX
