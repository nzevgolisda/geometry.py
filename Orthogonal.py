from math import pi
from numpy import real as RE
from math import acos
from math import pi
from cmath import pi
import cmath
import math
from Vector import Vector
v0 = Vector(0, 0)

class Orthogonal(Vector):
    def __init__(self, vectorA, vectorB, vectorC, vectorD):
        self.A = vectorA
        self.B = vectorB
        self.C = vectorC
        self.D = vectorD
        self.initSides()
        self.initAngles()
    def initSides(self):
        self.sideAB = (self.B).Sub(self.A)
        self.sideBC = (self.C).Sub(self.B)
        self.sideCD = (self.D).Sub(self.C)
        self.sideDA = (self.A).Sub(self.D)
        self.sides = [self.sideAB, self.sideBC, self.sideCD, self.sideDA]
    def initAngles(self):
        self.angleA = ((self.sideAB).Angle(self.sideCD))
        self.angleB = ((self.sideBC).Angle(self.sideAB))
        self.angleC = ((self.sideCD).Angle(self.sideBC))
        self.angleD = ((self.sideCD).Angle(self.sideDA))
        self.angles = [self.angleA, self.angleB, self.angleC, self.angleD]
    def isTrueOrth(self):
        for index in range(1):
            if (self.sides[index]).Abs() == (self.sides[index + 2]).Abs():
                if ((self.sides[index + 1]).linearInd(self.sides[index + 3]) == False):
                    sum_0 = v0
                    for side in self.sides:
                        sum_0 = sum_0.Add(side)
                    if sum_0 == v0:
                        sum_1 = 0.0
                        for angle in self.angles:
                            sum_1 = sum_1 + angle
                        if sum_1 != 2 * pi:    
                            return False
                        else:
                            return True
    def trueSquare(self):
        countFalse = 0
        recent = self.sides
        numS = len(recent)
        side_0 = self.sides[0]
        for Index in range(1, numS + 1):
            side_1 = self.sides[Index]
            if side_0.linearInd(side_1) == False:
                countFalse = countFalse + 1
            else:
                side_0 = side_1
        if countFalse == 0:
            return True
        else:
            return False
    