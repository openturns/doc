#! /usr/bin/env python

from __future__ import print_function
from openturns import *


# BEGIN_TEX
class RVEC(PythonRandomVector):

    def __init__(self):
        PythonRandomVector.__init__(self, 2)
        self.setDescription(['R', 'S'])

    def getRealization(self):
        X = [RandomGenerator.Generate(), 2 + RandomGenerator.Generate()]
        return X

    def getSample(self, size):
        X = []
        for i in range(size):
            X.append(
                [RandomGenerator.Generate(), 2 + RandomGenerator.Generate()])
            return X

    def getMean(self):
        return [0.5, 2.5]

    def getCovariance(self):
        return [[0.0833333, 0.0], [0.0, 0.0833333]]

R = RVEC()
myRV = RandomVector(R)
# END_TEX
