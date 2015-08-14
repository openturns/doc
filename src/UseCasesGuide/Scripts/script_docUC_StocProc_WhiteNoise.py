from __future__ import print_function
from openturns import *
from math import *

# Create the distribution of dimension  3
# Care : the mean must be NULL
myDist = Normal(3)

# Define a bi dimensional mesh
vertices = [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0],
            [1.5, 1.0], [2.0, 1.5], [0.5, 1.5]]
simplicies = IndicesCollection(
    [[0, 1, 2], [1, 2, 3], [2, 3, 4], [2, 4, 5], [0, 2, 5]])
myMesh = Mesh(vertices, simplicies)

# BEGIN_TEX
# Create  a white noise
myWN = WhiteNoise(myDist, myMesh)
# END_TEX
