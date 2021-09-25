from numpy import real as RE
from math import acos
from math import pi
from cmath import pi
import cmath
import math
class Vector:
    def __init__(self, x_Axis, y_Axis):
        self.x = x_Axis
        self.y = y_Axis
    def Add(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def Sub(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    def InnProd(self, other):
        REx = self.x * other.x
        IMy = self.y * other.y
        Sum = REx + IMy
        return Sum ** (0.5)
    def mulBy(self, el):
        self.x = self.x * el
        self.y = self.y * el
        return self
    def Abs(self):
        Sum = (self.x) ** 2 + (self.y) ** 2
        return Sum ** 0.5
    def dist(self, other):
        return self.Sub(other).Abs()
    def Clone(self):
        v = Vector(self.x, self.y)
        return v
    def Angle(self, other):
        if (self == Vector(0, 0) or other == Vector(0, 0)):
            return str('theta in [0, 2π]')
        else:
            y = self.InnProd(other)
            z = other.InnProd(other)
            w = self.InnProd(self)
            return RE(cmath.acos((y / (z * w))))
    def IsEqual(self, other):
        return (self.x == other.x and self.y == other.y)
    def linearInd(self, other):
        y = self.InnProd(other)
        z = other.InnProd(other)
        w = self.InnProd(self)
        theta = RE(cmath.acos(y / (z * w)))
        if self.InnProd(other) == 0:
            return True
        else:
            e = 0.1
            if theta < e and theta > -e:
                return False
            elif theta < math.pi + e and theta > math.pi - e:
                return False 
            else:
                return True    
    def printV(self):
        return print((self.x, self.y))

  ##  