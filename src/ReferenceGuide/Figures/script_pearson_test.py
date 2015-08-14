from openturns import *

size = 5
RandomGenerator.SetSeed(0)
# Data
x1 = Uniform(1.0, 9.0).getSample(size)
y1 = Uniform(0.0, 120.0).getSample(size)
# Linear model
algo = LinearLeastSquares(x1, y1)
algo.run()
linear = algo.getResponseSurface()

graph = Graph("Non significant Pearson coefficient", "u", "v", True, "")
cloud1 = Cloud(x1, y1)
cloud1.setPointStyle("diamond")
cloud1.setColor("orange")
cloud1.setLineWidth(2)
graph.add(cloud1)
curve1 = Curve(x1, linear(x1))
curve1.setColor("black")
curve1.setLineWidth(2)
graph.add(curve1)
minPoint = NumericalPoint(2)
minPoint[0] = 0.0
minPoint[1] = 0.0
maxPoint = NumericalPoint(2)
maxPoint[0] = 10.0
maxPoint[1] = 120.0
bbox = Interval(minPoint, maxPoint)
graph.setBoundingBox(bbox)
graph.draw("pearson2", 600, 600, GraphImplementation.PDF)

size = 50 - size

# Data
x2 = Uniform(1.0, 9.0).getSample(size)
y2 = Uniform(0.0, 120.0).getSample(size)
# Merge with previous data
x = NumericalSample(x1)
y = NumericalSample(y1)
for i in range(size):
    x.add(x2[i])
    y.add(y2[i])
    # Linear model
    algo = LinearLeastSquares(x, y)
    algo.run()
    linear = algo.getResponseSurface()

graph = Graph("Null Pearson coefficient", "u", "v", True, "")
graph.add(cloud1)
cloud2 = Cloud(x2, y2)
cloud2.setPointStyle("square")
cloud2.setColor("blue")
cloud2.setLineWidth(2)
graph.add(cloud2)
curve2 = Curve(x, linear(x))
curve2.setColor("black")
curve2.setLineWidth(2)
graph.add(curve2)
graph.setBoundingBox(bbox)
graph.draw("pearson3", 600, 600, GraphImplementation.PDF)
