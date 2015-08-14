from __future__ import print_function
from openturns import *

# Create a mesh

# BEGIN_TEX
########################
# Case 1: Define a mesh from its vertices and simplices

# Define a one dimensional mesh
vertices = [[0.5], [1.5], [2.1], [2.7]]
simplicies = IndicesCollection([[0, 1], [1, 2], [2, 3]])
myMesh1D = Mesh(vertices, simplicies)

# Define a bi dimensional mesh
vertices = [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0],
            [1.5, 1.0], [2.0, 1.5], [0.5, 1.5]]
simplicies = IndicesCollection(
    [[0, 1, 2], [1, 2, 3], [2, 3, 4], [2, 4, 5], [0, 2, 5]])
myMesh2D = Mesh(vertices, simplicies)

# Import a mesh from a MSHFile
# myMSHmesh=Mesh.ImportFromMSHFile('myMSHFile.msh')

# Draw the mesh
mygraph1 = myMesh1D.draw()
# Show(mygraph1)
mygraph2 = myMesh2D.draw()
# Show(mygraph2)

########################
# Case 2: Define a mesh which is regularly meshed box
# in dimension 1 or 2

# Define the number of intervals in each direction of the box
myIndices = Indices([5, 10])
myMesher = IntervalMesher(myIndices)

# Create the mesh of the box [0., 2.] * [0., 4.]
lowerBound = [0., 0.]
upperBound = [2., 4.]
myInterval = Interval(lowerBound, upperBound)
myMeshBox = myMesher.build(myInterval)
mygraph3 = myMeshBox.draw()
# Show(mygraph3)

# END_TEX
