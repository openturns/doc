from openturns import *
from openturns.viewer import View


scaledVector = NumericalPoint(2)
scaledVector[0] = 1.5
scaledVector[1] = 2.5

translationVector = NumericalPoint(2)
translationVector[0] = 2
translationVector[1] = 3


levels = NumericalPoint(3)
levels[0] = 1
levels[1] = 1.5
levels[2] = 3.

#############################################
# Experiment plane : Composite

# grid point
myCompositePlane = Composite(2,levels)
myCompositePlaneGrid = myCompositePlane.generate()

drawableCompositeGrid = Cloud(myCompositePlaneGrid, "blue", "square", "Composite Grid")
graphCompositeGrid = Graph("Composite Grid", "x", "y", True)
graphCompositeGrid.add(drawableCompositeGrid)
graphCompositeGrid.draw("CompositeGrid")
#View(graphCompositeGrid).show()

# scaled grid
myCompositePlaneGrid.scale(scaledVector)
drawableScaledCompositeGrid = Cloud(myCompositePlaneGrid, "blue", "circle", "Composite Grid")
graphScaledCompositeGrid = Graph("Scaled Composite Grid", "x", "y", True)
graphScaledCompositeGrid.add(drawableScaledCompositeGrid)
graphScaledCompositeGrid.draw("ScaledCompositeGrid")
#View(graphScaledCompositeGrid).show()


# Translated grid
myCompositePlaneGrid.translate(translationVector)
drawableTranslatedScaledCompositeGrid = Cloud(myCompositePlaneGrid, "blue", "triangleup", "Composite Grid")
graphTranslatedScaledCompositeGrid = Graph("Translated Scaled Composite Grid", "x", "y", True)
graphTranslatedScaledCompositeGrid.add(drawableTranslatedScaledCompositeGrid)
graphTranslatedScaledCompositeGrid.draw("TranslatedScaledCompositeGrid")
#View(graphTranslatedScaledCompositeGrid).show()



#############################################
# Experiment plane : Factorial

# grid points
myFactorialPlane = Factorial(2,levels)
myFactorialPlaneGrid = myFactorialPlane.generate()

drawableFactorialGrid = Cloud(myFactorialPlaneGrid, "blue", "square", "Factorial Grid")
graphFactorialGrid = Graph("Factorial Grid", "x", "y", True)
graphFactorialGrid.add(Drawable(drawableFactorialGrid))
graphFactorialGrid.draw("FactorialGrid")
#View(graphFactorialGrid).show()

# scaled grid
myFactorialPlaneGrid.scale(scaledVector)
drawableScaledFactorialGrid = Cloud(myFactorialPlaneGrid, "blue", "circle", "Factorial Grid")
graphScaledFactorialGrid = Graph("Scaled Factorial Grid", "x", "y", True)
graphScaledFactorialGrid.add(drawableScaledFactorialGrid)
graphScaledFactorialGrid.draw("ScaledFactorialGrid")
#View(graphScaledFactorialGrid).show()


# Translated grid
myFactorialPlaneGrid.translate(translationVector)
drawableTranslatedScaledFactorialGrid = Cloud(myFactorialPlaneGrid, "blue", "triangleup", "Factorial Grid")
graphTranslatedScaledFactorialGrid = Graph("Translated Scaled Factorial Grid", "x", "y", True)
graphTranslatedScaledFactorialGrid.add(drawableTranslatedScaledFactorialGrid)
graphTranslatedScaledFactorialGrid.draw("TranslatedScaledFactorialGrid")
#View(graphTranslatedScaledFactorialGrid).show()

#############################################
# Experiment plane : Axial

# grid points
myAxialPlane = Axial(2,levels)
myAxialPlaneGrid = myAxialPlane.generate()

drawableAxialGrid = Cloud(myAxialPlaneGrid, "blue", "square", "Axial Grid")
graphAxialGrid = Graph("Axial Grid", "x", "y", True)
graphAxialGrid.add(drawableAxialGrid)
graphAxialGrid.draw("AxialGrid")
#View(graphAxialGrid).show()

# scaled grid
myAxialPlaneGrid.scale(scaledVector)
drawableScaledAxialGrid = Cloud(myAxialPlaneGrid, "blue", "circle", "Axial Grid")
graphScaledAxialGrid = Graph("Scaled Axial Grid", "x", "y", True)
graphScaledAxialGrid.add(drawableScaledAxialGrid)
graphScaledAxialGrid.draw("ScaledAxialGrid")
#View(graphScaledAxialGrid).show()


# Translated grid
myAxialPlaneGrid.translate(translationVector)
drawableTranslatedScaledAxialGrid = Cloud(myAxialPlaneGrid, "blue", "triangleup", "Axial Grid")
graphTranslatedScaledAxialGrid = Graph("Translated Scaled Axial Grid", "x", "y", True)
graphTranslatedScaledAxialGrid.add(drawableTranslatedScaledAxialGrid)
graphTranslatedScaledAxialGrid.draw("TranslatedScaledAxialGrid")
#View(graphTranslatedScaledAxialGrid).show()



#############################################
# Experiment plane : Box

# grid points
discretisation = NumericalPoint(2)
discretisation[0] = 4
discretisation[1] = 2.

myBoxPlane = Box(discretisation)
myBoxPlaneGrid = myBoxPlane.generate()

drawableBoxGrid = Cloud(myBoxPlaneGrid, "blue", "square", "Box Grid")
graphBoxGrid = Graph("Box Grid", "x", "y", True)
graphBoxGrid.add(drawableBoxGrid)
graphBoxGrid.draw("BoxGrid")
#View(graphBoxGrid).show()


# scaled grid
myBoxPlaneGrid.scale(scaledVector)
drawableScaledBoxGrid = Cloud(myBoxPlaneGrid, "blue", "circle", "Box Grid")
graphScaledBoxGrid = Graph("Scaled Box Grid", "x", "y", True)
graphScaledBoxGrid.add(drawableScaledBoxGrid)
graphScaledBoxGrid.draw("ScaledBoxGrid")
#View(graphScaledBoxGrid).show()



# Translated grid
myBoxPlaneGrid.translate(translationVector)
drawableTranslatedScaledBoxGrid = Cloud(myBoxPlaneGrid, "blue", "triangleup", "Box Grid")
graphTranslatedScaledBoxGrid = Graph("Translated Scaled Box Grid", "x", "y", True)
graphTranslatedScaledBoxGrid.add(drawableTranslatedScaledBoxGrid)
graphTranslatedScaledBoxGrid.draw("TranslatedScaledBoxGrid")
#View(graphTranslatedScaledBoxGrid).show()
