from openturns import *

size = 6
RandomGenerator.SetSeed(3)

# Data
x1 = Uniform(1.0, 9.0).getSample(size)
y1 = Uniform(0.0, 120.0).getSample(size)
# Quadratic model
algo = QuadraticLeastSquares(x1, y1)
algo.run()
quadratic = algo.getResponseSurface()

graph = Graph("Non significant Spearman coefficient", "u", "v", True, "")
cloud1 = Cloud(x1, y1)
cloud1.setPointStyle("diamond")
cloud1.setColor("orange")
cloud1.setLineWidth(2)
graph.add(cloud1)
xMin = x1.getMin()
xMax = x1.getMax()
yMin = y1.getMin()
yMax = y1.getMax()
npts = 100
lx = NumericalSample(npts, 1)
ly = NumericalSample(npts, 1)
for i in range(npts):
    lx[i] = xMin + (xMax - xMin) * (float(i) / float(npts - 1))
    ly[i] = quadratic(lx[i])
    curve1 = Curve(lx, ly)
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
    graph.draw("spearman2", 600, 600, GraphImplementation.PDF)

size = 150 - size

# Data
x2 = Uniform(1.0, 9.0).getSample(size)
y2 = Uniform(0.0, 120.0).getSample(size)
# Merge with previous data
x = NumericalSample(x1)
y = NumericalSample(y1)
for i in range(size):
    x.add(x2[i])
    y.add(y2[i])
    # Quadratic model
    algo = QuadraticLeastSquares(x, y)
    algo.run()
    quadratic = algo.getResponseSurface()

graph = Graph("Null Spearman coefficient", "u", "v", True, "")
graph.add(cloud1)
cloud2 = Cloud(x2, y2)
cloud2.setPointStyle("square")
cloud2.setColor("blue")
cloud2.setLineWidth(2)
graph.add(cloud2)
xMin = x.getMin()
xMax = x.getMax()
yMin = y.getMin()
yMax = y.getMax()
npts = 100
lx = NumericalSample(npts, 1)
ly = NumericalSample(npts, 1)
for i in range(npts):
    lx[i] = xMin + (xMax - xMin) * (float(i) / float(npts - 1))
    ly[i] = quadratic(lx[i])
    curve2 = Curve(lx, ly)
    curve2.setColor("black")
    curve2.setLineWidth(2)
    graph.add(curve2)
    graph.setBoundingBox(bbox)
    graph.draw("spearman3", 600, 600, GraphImplementation.PDF)
