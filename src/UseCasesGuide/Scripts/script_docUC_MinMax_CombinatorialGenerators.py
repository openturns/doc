from __future__ import print_function
from openturns import *

# BEGIN_TEX
# Create the generator of the Cartesian product {0,...,3}x{0,...,5}x{0,...,8}
myTuplesGenerator = Tuples([4, 6, 9])
# Generate all the tuples
myTuples = myTuplesGenerator.generate()

# Create the generator of the injective functions from {0,...,3} into {0,...,5}
myKPermutationsGenerator = KPermutations(4, 6)
# Generate all the injective functions
myKPermutations = myKPermutationsGenerator.generate()

# Create the generator of the subsets of {0,...,5} with 4 elements
myCombinationsGenerator = Combinations(4, 6)
# Generate all the subsets
myKPermutations = myKPermutationsGenerator.generate()
# END_TEX
