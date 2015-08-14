#! /usr/bin/env python
from openturns import *
from math import pi, sqrt

# Add a missing entry in the ResourceMap object
ResourceMap.SetAsNumericalScalar("BoxCox-RootEpsilon", 1.0e-6)

# 0) TimeGrid and WhiteNoise
# TimeGrid has dt 0.5 /pi such as the frequency grid correspond to a Fourier grid
Tmin = 0.0
deltaT = 0.5 / pi
steps = 2048

# Initialization of the TimeGrid
timeGrid = RegularGrid(Tmin, deltaT, steps)

# Distributions for the  choice
# for the tests, gaussian white noise or uniform even if the likelihood writes for a gaussian noise
sigma = 0.01
isGaussianNoise = True
if isGaussianNoise:
  dist = Normal(0.0, sigma)
else :
  a = sqrt(3) * sigma
  dist = Uniform(-a, a)

# WhiteNoise definition
epsilon = WhiteNoise(dist, timeGrid)

#----------------------------------------#
#----------------------------------------#
#-- Differents models are investigated --#
#----------------------------------------#
#----------------------------------------#
#  Models ivestigated :
# 1) ARMA(3, 0) or AR(3)
# 2) ARMA(1, 1)
# 3) ARMA(0, 1) or MA(1)
# 4) ARMA(0, 2) or MA(3)
# 5) ARMA()
# Estimation is done on 1 realization and one sample of realizations

#----------------------------------------#
#------------ AR(3) estimate ------------#
#----------------------------------------#
# AR coefficients
arCoefficients = NumericalPoint([0.8, 0.3, 0.4])
coefficientsP = ARMACoefficients(arCoefficients)
p = arCoefficients.getSize()

# MA coefficients
q = 0
coefficientsQ = ARMACoefficients(q, 1)

model1 = ARMA(coefficientsP, coefficientsQ, epsilon)

# realization
realization1 = model1.getRealization()
sample1 = model1.getSample(100)
factory = WhittleFactory(p, q)
myARMA1 = factory.build(realization1)
myARMASample1 = factory.build(sample1)

print "\nModel 1"
print "Exact model: ", model1
print "Estimated model with one realization : ", myARMA1
print "Estimated model with one sample : ", myARMASample1

#----------------------------------------#
#---------- ARMA(1,1) estimate ----------#
#----------------------------------------#
# AR coefficients
arCoefficients = NumericalPoint([0.8])
coefficientsP = ARMACoefficients(arCoefficients)
p = arCoefficients.getSize()

# MA coefficients
maCoefficients = NumericalPoint([1.05])
coefficientsQ = ARMACoefficients(maCoefficients)
q = maCoefficients.getSize()

model2 = ARMA(coefficientsP, coefficientsQ, epsilon)

# realization2
realization2 = model2.getRealization()
sample2 = model2.getSample(100)

factory = WhittleFactory(p, q)
myARMA2 = factory.build(realization2)
myARMASample2 = factory.build(sample2)

print "\nModel 2"
print "Exact model: ", model2
print "Estimated model with one realization : ", myARMA2
print "Estimated model with one sample : ", myARMASample2

#----------------------------------------#
#------------ MA(1) estimate ------------#
#----------------------------------------#
# AR coefficients
coefficientsP = ARMACoefficients(0, 1)
p = 0

# MA coefficients
maCoefficients = NumericalPoint([0.8])
coefficientsQ = ARMACoefficients(maCoefficients)
q = maCoefficients.getSize()

model3 = ARMA(coefficientsP, coefficientsQ, epsilon)

# realization2
realization3 = model3.getRealization()
sample3 = model3.getSample(100)

factory = WhittleFactory(p, q)
myARMA3 = factory.build(realization3)
myARMASample3 = factory.build(sample3)

print "\nModel 3"
print "Exact model: ", model3
print "Estimated model: ", myARMA3
print "Estimated model with one sample : ", myARMASample3

#----------------------------------------#
#------------ MA(2) estimate ------------#
#----------------------------------------#
# AR coefficients
coefficientsP = ARMACoefficients(0, 1)
p = 0

# MA coefficients
maCoefficients = NumericalPoint([0.7, 0.4])
coefficientsQ = ARMACoefficients(maCoefficients)
q = maCoefficients.getSize()

model4 = ARMA(coefficientsP, coefficientsQ, epsilon)

# realization2
realization4 = model4.getRealization()
sample4 = model4.getSample(100)

factory = WhittleFactory(p, q)
myARMA4 = factory.build(realization4)
myARMASample4 = factory.build(sample4)

print "\nModel 4"
print "Exact model: ", model4
print "Estimated model with one realization : ", myARMA4
print "Estimated model with one sample : ", myARMASample4

#----------------------------------------#
#---------- ARMA(2,1) estimate ----------#
#----------------------------------------#
# AR coefficients
arCoefficients = NumericalPoint([0.8, 0.9])
coefficientsP = ARMACoefficients(arCoefficients)
p = arCoefficients.getSize()

# MA coefficients
maCoefficients = NumericalPoint([1.0])
coefficientsQ = ARMACoefficients(maCoefficients)
q = maCoefficients.getSize()

model5 = ARMA(coefficientsP, coefficientsQ, epsilon)

# realization2
realization5 = model5.getRealization()
sample5 = model5.getSample(100)

factory = WhittleFactory(p, q)
myARMA5 = factory.build(realization5)
myARMASample5 = factory.build(sample5)

print "\nModel 5"
print "Exact model: ", model5
print "Estimated model with one realization : ", myARMA5
print "Estimated model with one sample : ", myARMASample5
