from __future__ import print_function
from openturns import *

# Create a sample froma  continuous distribution
# For example form the beta distribution
dist_cont = Beta(2.0, 4.0, 0.0, 1.)
# View(dist_cont.drawPDF()).show()
N = 1000
sample_cont = dist_cont.getSample(N)

# Create a sample froma  discrete distribution
# For example form the beta distribution
dist_disc = Poisson(2.0)
# View(dist_disc.drawPDF()).show()
N = 1000
sample_disc = dist_disc.getSample(N)

# BEGIN_TEX
##################################
# CASE 1 : Continuous distributions
##################################

##########################
# Specify the models only
# Then, OpenTURNS finds the best parameters and tests the distribution

# Create a collection of factories for all the models
# to be tested
collContFact = [BetaFactory()]

# Rank the continuous models by the Kolmogorov p-values :
bestContModelKol = FittingTest.BestModelKolmogorov(sample_cont, collContFact)

# Get all information on that distribution
print("best continuous distribution by Kolmogorov = ", bestContModelKol)

# Rank the continuous models wrt the BIC crieria :
bestContModelBIC = FittingTest.BestModelBIC(sample_cont, collContFact)

# Get all information on that distribution
print("best continuous distribution wrt BIC = ", bestContModelBIC)

##########################
# Specify the entire distributions (model + parameters)
# Then OpenTURNS tests the model

# Create a collection of the distributions to be tested
collContDist = [Beta(2.0, 4.0, 0.0, 1.), Triangular(0., 0.5, 1.)]

# Rank the continuous models by the Kolmogorov p-values :
bestcontDistKol = FittingTest.BestModelKolmogorov(sample_cont, collContDist)

# Get all information on that distribution
print("best continuous distribution by Kolmogorov = ", bestcontDistKol)

# Rank the continuous models wrt the BIC crieria :
bestContDistBIC = FittingTest.BestModelBIC(sample_cont, collContDist)

# Get all information on that distribution
print("best continuous distribution wrt BIC = ", bestContDistBIC)

##################################
# CASE 2 : Discrete distributions
##################################

##########################
# Specify the models only
# Then, OpenTURNS finds the best parameters and tests the distribution

# Create a collection of factories for all the models
# to be tested (here no idea for another discrete distributions ...)
collDiscFact = [PoissonFactory()]

# Rank the discrete models wrt the ChiSquared p-values :
bestDiscModelChiSq = FittingTest.BestModelChiSquared(sample_disc, collDiscFact)

# Get all information on that distribution
print("best discrete distribution by  = ", bestDiscModelChiSq)

# Rank the discrete models wrt the BIC crieria :
bestDiscDistBIC = FittingTest.BestModelBIC(sample_disc, collDiscFact)

# Get all information on that distribution
print("best discrete distribution wrt BIC = ", bestDiscDistBIC)

##########################
# Specify the entire distributions (model + parameters)
# Then OpenTURNS only tests the distributions

# Create a collection of the distributions to be tested
collDiscDist = [Poisson(2), Geometric(0.1)]

# Rank the discrete distributions wrt the ChiSquared p-values :
bestDiscDistChiSq = FittingTest.BestModelChiSquared(sample_disc, collDiscDist)

# Get all information on that distribution
print("best continuous distribution by  = ", bestDiscDistChiSq)

# Rank the discrete distributions wrt the BIC crieria :
bestDiscDistBIC = FittingTest.BestModelBIC(sample_disc, collDiscDist)

# Get all information on that distribution
print("best continuous distribution wrt BIC = ", bestDiscDistBIC)

# END_TEX
