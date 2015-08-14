from openturns import *

def meshBox(L, H, nx, ny):
    dx = float(L) / nx
    dy = float(H) / ny

    # First, build the vertices
    vertices = NumericalSample(0, 2)
    for i in range(nx+1):
        x = i * dx
        for j in range(ny+1):
            vertices.add([x, j * dy])

    # Second, build the simplices
    simplices = IndicesCollection(0, Indices(3))
    index = 0
    for i in range(0, nx):
        for j in range(ny):
            simplices.add([index, index + 1, index + ny + 1])
            simplices.add([index + 1, index + ny + 1, index + ny + 2])
            index += 1
            index += 1
            return Mesh(vertices, simplices)

# Define a bi dimensional mesh
myMesh = meshBox(2.0,1.0, 80, 40)

# Define a scalar temporal normal process on the mesh
amplitude=[1.0]
scale=[0.2]
myCovModel=ExponentialModel(amplitude,scale)

myProcess=TemporalNormalProcess(myCovModel, myMesh)

myField=myProcess.getRealization()

myGraph1=myField.drawMarginal(0, False)
myGraph1.setTitle('Field with no interpolation')
#Show(myGraph1)
myGraph1.draw('Field_nointerp', 800, 400, GraphImplementation.PNG)

myGraph2=myField.drawMarginal(0)
myGraph2.setTitle('Field with linear interpolation')
#Show(myGraph2)
myGraph2.draw('Field_interp', 800, 400, GraphImplementation.PNG)

myField.exportToVTKFile('myField.vtk')
