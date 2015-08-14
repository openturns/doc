from __future__ import print_function
from openturns import *

# BEGIN_TEX
#################################################
# GRAPH 1 : drawings of the 5-th first members of
# the Jacobi family
#################################################

# Create the Jacobi polynomials family using the default Jacobi.ANALYSIS
# parameter set
alpha = 0.5
beta = 1.5
jacobiFamily = JacobiFactory(alpha, beta)

# Fix the degree max of the polynomials
# which will be drawn
degreeMax = 5

# Load all the valid colors
colorList = Drawable.BuildDefaultPalette(degreeMax)

# Create a fine title
titleJacobi = "Jacobi(" + str(alpha) + ", " + str(beta) + ") polynomials"

# Create an empty graph which will be fullfilled
# with curves
graphJacobi = Graph(titleJacobi, "z", "polynomial values", True, "topright")

# Fix the number of points for the graph
pointNumber = 101

# Bounds of the graph
xMinJacobi = -1
xMaxJacobi = 1

# Get the curves
for i in range(degreeMax):
    graphJacobi_temp = jacobiFamily.build(i).draw(
        xMinJacobi, xMaxJacobi, pointNumber)
    graphJacobi_temp_draw = graphJacobi_temp.getDrawable(0)
    legend = "degree " + str(i)
    graphJacobi_temp_draw.setLegend(legend)
    graphJacobi_temp_draw.setColor(colorList[i])
    graphJacobi.add(graphJacobi_temp_draw)

# In order to see the graphs without creating the files .EPS, .PNG and .FIG
# Show(graphJacobi)

# END_TEX
