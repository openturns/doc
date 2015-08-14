from openturns import *
from math import *

# Time grid over which all the processes will be defined
nt = 100

timeGrid = RegularGrid(0.0, 1.0, nt)

# Definition of the distribution
sigma = 1.0
myDistribution = Normal(0., sigma)

# Definition of the process
myProcess = WhiteNoise(myDistribution, timeGrid)

# We get a realization of the white noise process
realization = myProcess.getRealization()


# The realization is a time series
# we draw it as function of time thanks to the drawMarginal method
# We rework the legend name and color to have pretty graph
graph = Graph()
marginalDraw = realization.drawMarginal(0)
drawable = marginalDraw.getDrawable(0)
drawable.setLegendName('realization')
drawable.setColor('blue')
graph.add(drawable)

graph.setXTitle('Time')
graph.setYTitle('Values')
graph.setTitle("White noise process")
graph.setLegendPosition('topright')
graph.draw("whitenoise_realization", 800, 600, GraphImplementation.PNG)
graph.draw("whitenoise_realization", 800, 600, GraphImplementation.PDF)

# Several realization ==> here we fix 5 in order to be able to compare and visualize difference
sample = myProcess.getSample(5)
graphSample = sample.drawMarginal(0)
graphSample.setTitle("5 realizations of the White noise process")
for k in range(5):
  drawable = graphSample.getDrawable(k)
  drawable.setLegendName('realization ' + str(k+1))
  graphSample.setDrawable(drawable, k)

graphSample.draw("whitenoise_realizations", 800, 600, GraphImplementation.PNG)
graphSample.draw("whitenoise_realizations", 800, 600, GraphImplementation.PDF)

# Whitenoise from a mesh
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

mesh = meshHearth(250, 40)
g0 = mesh.draw()
g0.setTitle("Bidimensional mesh")
g0.draw("Mesh", 800, 600, GraphImplementation.PNG)
wn = WhiteNoise(Normal())
wn.setMesh(mesh)
fld = wn.getRealization()
g1 = fld.drawMarginal(0, False)
g1.setTitle("White noise realization")
g1.draw("Field_nointerp", 800, 600, GraphImplementation.PNG)
g2 = fld.drawMarginal(0, True)
g2.setTitle("White noise realization")
g2.draw("Field_interp", 800, 600, GraphImplementation.PNG)
