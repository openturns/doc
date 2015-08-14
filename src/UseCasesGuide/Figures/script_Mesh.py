from openturns import *


# Define a one dimensional mesh
vertices = [[0.5], [1.5], [2.1], [2.7]]
simplicies = IndicesCollection([[0, 1], [1, 2], [2, 3]])
mesh1D = Mesh(vertices, simplicies)
graph1=mesh1D.draw()
graph1.setTitle('One dimensional mesh')
graph1.draw('mesh_oneD', 800, 600, GraphImplementation.PNG)

# Define a bi dimensional mesh
vertices = [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [1.5, 1.0], [2.0, 1.5], [0.5, 1.5]]
simplicies = IndicesCollection([[0, 1, 2], [1, 2, 3], [2, 3, 4], [2, 4, 5], [0, 2, 5]])
mesh2D = Mesh(vertices, simplicies)
graph2=mesh2D.draw()
graph2.setTitle('Bidimensional mesh')
graph2.setLegendPosition('bottomright')
Show(graph2)
graph2.draw('mesh_twoD', 800, 600, GraphImplementation.PNG)


# Create a mesh of dimension 2: the heart
def meshHearth(ntheta, nr):
    # First, build the nodes
    nodes = NumericalSample(0, 2)
    nodes.add([0.0, 0.0])
    for j in range(ntheta):
        theta = (pi * j) / ntheta
        if (abs(theta - 0.5 * pi) < 1e-10):
            rho = 2.0
        elif (abs(theta) < 1e-10) or (abs(theta-pi) < 1e-10):
            rho = 0.0
        else:
            absTanTheta = abs(tan(theta));
            rho = absTanTheta**(1/absTanTheta) + sin(theta)
            cosTheta = cos(theta)
            sinTheta = sin(theta)
            for k in range(nr):
                tau = (k + 1.0) / nr
                r = rho * tau
                nodes.add([r * cos(theta), r * sin(theta) - tau])
                # Second, build the triangles
                triangles = IndicesCollection(0, Indices(3))
                # First hearth
                for j in range(ntheta):
                    triangles.add([0, 1 + j * nr, 1 + ((j + 1) % ntheta)* nr])
                    # Other hearths
                    for j in range(ntheta):
                        for k in range(nr-1):
                            i0 = k + 1 + j * nr
                            i1 = k + 2 + j * nr
                            i2 = k + 2 + ((j + 1) % ntheta) * nr
                            i3 = k + 1 + ((j + 1) % ntheta) * nr
                            triangles.add([i0, i1, i2])
                            triangles.add([i0, i2, i3])

    return Mesh(nodes, triangles)

myMesh = meshHearth(250, 40)

graphMesh=myMesh.draw()
graphMesh.setTitle('Bidimensional mesh')
graphMesh.setLegendPosition('')
Show(graphMesh)
graphMesh.draw('meshHeart', 800, 600, GraphImplementation.PNG)
#graphMesh.draw('meshHeart', 800, 600, GraphImplementation.PDF)


########################
# Case 2: Define a mesh wich is regularly meshed box
# in dimension 1 or 2

# Define the number of interval in each direction of the box
myIndices= Indices([5,10])
myMesher=IntervalMesher(myIndices)

# Create the mesh of the box [0., 2.] * [0., 4.]
lowerBound=[0., 0.]
upperBound=[2., 4.]
myInterval = Interval(lowerBound, upperBound)
myMeshBox=myMesher.build(myInterval)
mygraph3=myMeshBox.draw()
mygraph3.setTitle('Bidimensional mesh on a box')
#Show(mygraph3)
mygraph3.draw('meshBox', 800, 600, GraphImplementation.PNG)


########################
# Case 3: Define a mesh wich is regularly meshed box
# and Transform it through a fuunction

from math import *

myIndices= Indices([50,50])
myMesher=IntervalMesher(myIndices)
# r in [1., 2.] and theta in (0., pi]
lowerBound2=[1., 0.]
upperBound2=[2., pi]
myInterval = Interval(lowerBound2, upperBound2)
myMeshBox2=myMesher.build(myInterval)

# define the mapping function
#f=NumericalMathFunction(['r', 'theta'], ['r*cos(theta)', 'r*sin(theta)'])
f=NumericalMathFunction(['r', 'theta'], ['r*cos(theta)*cos(5*theta)', 'r*sin(theta)*sin(8*theta)'])
oldVertices=myMeshBox2.getVertices()
newVertices=f(oldVertices)
myMeshBox2.setVertices(newVertices)
Show(myMeshBox2.draw())

graphMappedBox=myMeshBox2.draw()
graphMappedBox.setTitle('Mapped box mesh')
graphMappedBox.draw('MappedBox', 800, 800, GraphImplementation.PNG)
