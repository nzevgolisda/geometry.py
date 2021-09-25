from Vector import Vector
from math import acos
from numpy import real as RE
from math import acos
from math import pi
from cmath import pi
import cmath
import math
from cmath import pi

class Circle:
    def __init__(self, center, rad):
        self.center = Vector(center.x, center.y)
        self.rad = rad
    def distCenter(self, otherVector):
        return (self.center).dist(otherVector)