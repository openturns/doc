from openturns import *
#
# Number of input random variables
dim=10
#
#===================================================================
#                         Marginal PDFs
#===================================================================
#
# Young's moduli
distE1 = LogNormal(210.e9,0.10,0.,LogNormal.MU_SIGMAOVERMU)  # Mean in Pa
distE2 = LogNormal(210.e9,0.10,0.,LogNormal.MU_SIGMAOVERMU)  # Mean in Pa
distE3 = LogNormal(210.e9,0.10,0.,LogNormal.MU_SIGMAOVERMU)  # Mean in Pa
# Cross-section areas
distS1 = Normal(0.0015,0.0015*0.05)   # Mean in m**2
distS2 = Normal(0.0015,0.0015*0.05)   # Mean in m**2
distS3 = Normal(0.0015,0.0015*0.05)   # Mean in m**2
# Point load
distP = Normal(250000.,250000.*0.20)  # Mean in N
#Load direction
distTheta =  Normal(45.,45.*0.03)     # Mean in degrees
# Angle (bar1-bar3)
distalpha1 = Normal(45.,45.*0.03)     # Mean in degrees
# Angle (bar2-bar3)
distalpha2 = Normal(45.,45.*0.03)     # Mean in degrees
#
#===================================================================
#                     Input random vector
#===================================================================
#
myCollection = DistributionCollection(dim)
myCollection[0] = distE1
myCollection[1] = distE2
myCollection[2] = distE3
myCollection[3] = distS1
myCollection[4] = distS2
myCollection[5] = distS3
myCollection[6] = distP
myCollection[7] = distTheta
myCollection[8] = distalpha1
myCollection[9] = distalpha2
myDistribution = ComposedDistribution(myCollection)
vectX = RandomVector(myDistribution)
