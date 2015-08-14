#! /usr/bin/env python

from __future__ import print_function
from openturns import *

# BEGIN_TEX
from math import *


class PDIST(PythonDistribution):

    def __init__(self, a=[0.0], b=[1.0]):
        super(PDIST, self).__init__(len(a))
        self.a = a
        self.b = b

    def getRange(self):
        return [self.a, self.b, [True] * len(self.a), [True] * len(self.a)]

    def getRealization(self):
        X = []
        for i in range(len(self.a)):
            X.append(
                self.a[i] + (self.b[i] - self.a[i]) * RandomGenerator.Generate())
        return X

    def getSample(self, size):
        X = []
        for i in range(size):
            X.append(self.getRealization())
        return X

    def computeCDF(self, X):
        cdf = 1.0
        for i in range(len(self.a)):
            cdf *= min(1.0,
                       max(0.0, (X[i] - self.a[i]) / (self.b[i] - self.a[i])))
        return cdf

    def computePDF(self, X):
        pdf = 1.0
        for i in range(len(self.a)):
            if (X[i] < self.a[i]) or (X[i] > self.b[i]):
                return 0.0
            pdf /= (self.b[i] - self.a[i])
        return pdf

    def getMean(self):
        mu = []
        for i in range(len(self.a)):
            mu.append(0.5 * (self.a[i] + self.b[i]))
        return mu

    def getStandardDeviation(self):
        stdev = []
        for i in range(len(self.a)):
            stdev.append((self.b[i] - self.a[i]) / sqrt(12.))
        return stdev

    def getSkewness(self):
        return [0.] * len(self.a)

    def getKurtosis(self):
        return [1.8] * len(self.a)

    def getStandardMoment(self, n):
        if n % 2 == 1:
            return [0.] * len(self.a)
        return [1. / (n + 1.)] * len(self.a)

    def getMoment(self, n):
        return [-0.1 * n] * len(self.a)

    def getCenteredMoment(self, n):
        return [0.] * len(self.a)

    def computeCharacteristicFunction(self, x):
        if len(self.a) > 1:
            raise ValueError('dim>1')
        ax = self.a[0] * x
        bx = self.b[0] * x
        return (sin(bx) - sin(ax) + 1j * (cos(ax) - cos(bx))) / (bx - ax)

    def isElliptical(self):
        return (len(self.a) == 1) and (self.a[0] == -self.b[0])

    def isCopula(self):
        for i in range(len(self.a)):
            if self.a[i] != 0.0:
                return False
            if self.b[i] != 1.0:
                return False
        return True

R = PDIST([1.0, 1.5], [2.0, 3.5])
myDist = Distribution(R)
#Show(myDist.drawPDF([0.0, 0.5], [3.0, 4.5]))

# END_TEX
