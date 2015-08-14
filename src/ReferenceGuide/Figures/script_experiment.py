from openturns import *

# Axial
d = Axial([1.5, 2.5, 3.5], [1, 2, 3])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("Axial experiment")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("Axial_DOE", 400, 420, GraphImplementation.PDF)
g.draw("Axial_DOE", 400, 420, GraphImplementation.PNG)
# Factorial
d = Factorial([1.5, 2.5, 3.5], [1, 2, 3])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("Factorial experiment")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("Factorial_DOE", 400, 420, GraphImplementation.PDF)
g.draw("Factorial_DOE", 400, 420, GraphImplementation.PNG)
# Composite
d = Composite([1.5, 2.5, 3.5], [1, 2, 3])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("Composite experiment")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("Composite_DOE", 400, 420, GraphImplementation.PDF)
g.draw("Composite_DOE", 400, 420, GraphImplementation.PNG)
# Box
d = Box([3, 4, 5])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("Box experiment")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("Box_DOE", 400, 420, GraphImplementation.PDF)
g.draw("Box_DOE", 400, 420, GraphImplementation.PNG)
# Combinations
d = Combinations(3, 12)
s = NumericalSample(d.generate())
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("Combinations generator")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("Combinations_DOE", 400, 420, GraphImplementation.PDF)
g.draw("Combinations_DOE", 400, 420, GraphImplementation.PNG)
# KPermutations
d = KPermutations(3, 12)
s = NumericalSample(d.generate())
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("KPermutations generator")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("KPermutations_DOE", 400, 420, GraphImplementation.PDF)
g.draw("KPermutations_DOE", 400, 420, GraphImplementation.PNG)
# Tuples
d = Tuples([3, 4, 5])
s = NumericalSample(d.generate())
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("Tuples generator")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("Tuples_DOE", 400, 420, GraphImplementation.PDF)
g.draw("Tuples_DOE", 400, 420, GraphImplementation.PNG)
# MonteCarlo
d = MonteCarloExperiment(ComposedDistribution([Uniform(), Uniform(), Uniform()]), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("MonteCarlo experiment")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("MonteCarlo_DOE", 400, 420, GraphImplementation.PDF)
g.draw("MonteCarlo_DOE", 400, 420, GraphImplementation.PNG)
# LHS
d = LHSExperiment(ComposedDistribution([Uniform(), Uniform(), Uniform()]), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("LHS experiment")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("LHS_DOE", 400, 420, GraphImplementation.PDF)
g.draw("LHS_DOE", 400, 420, GraphImplementation.PNG)
# Sobol
d = LowDiscrepancyExperiment(SobolSequence(), ComposedDistribution([Uniform(), Uniform(), Uniform()]), 32)
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("LHS experiment")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("Sobol_DOE", 400, 420, GraphImplementation.PDF)
g.draw("Sobol_DOE", 400, 420, GraphImplementation.PNG)
# GaussProduct
d = GaussProductExperiment(ComposedDistribution([Uniform(), Uniform(), Uniform()]), [4,6,8])
s = d.generate()
s.setDescription(["X1", "X2", "X3"])
g = Graph()
g.setTitle("LHS experiment")
g.setGridColor("black")
p = Pairs(s)
g.add(p)
g.draw("Gauss_DOE", 400, 420, GraphImplementation.PDF)
g.draw("Gauss_DOE", 400, 420, GraphImplementation.PNG)
