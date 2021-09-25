from math import acos
from numpy import real as RE
from math import acos
from math import pi
from cmath import pi
import cmath
import math
from cmath import pi
import math
from Vector import Vector
class Triangle:
    def __init__(self, vectorA, vectorB, vectorC):
        self.A = vectorA
        self.B = vectorB
        self.C = vectorC
        self.initSides()
        self.initAngles()
    def initSides(self):
        self.sideAB = self.B.Sub(self.A)
        self.sideBC = self.C.Sub(self.B)
        self.sideCA = self.A.Sub(self.C)
        self.sides = [self.sideAB, self.sideBC, self.sideCA]
    def initAngles(self):
        self.angleA = self.sideAB.Angle(self.sideCA)
        self.angleB = self.sideBC.Angle(self.sideAB)
        self.angleC = self.sideCA.Angle(self.sideBC)
        self.angles = [self.angleA, self.angleB, self.angleC]
    def isTrueTriangle(self):
        v0 = Vector(0, 0)
        sum_0 = v0
        for side in self.sides:
            sum_0 = sum_0.Add(side)
        if sum_0.IsEqual(v0):
            sum_1 = 0.0
            for angle in self.angles:
                sum_1 = sum_1 + angle
            #if sum_1 != pi:
            if sum_1 < 3.1 and sum_1 > 3.2:
                return False
            else:
                return True
    def orthTriangle(self):
        flag = 0
        n = 600
        for angle in self.angles:
            count = 0
            for index in range(1, n):
                if angle - 1/index <= math.pi/2 and angle - 1/index >= -math.pi/2:
                    count += 1
                else:
                    continue
            if count >= 3 * n / 4:
                flag += 1
            else:
                continue
        if flag == 0:
            return False
        else:
            return True
