from Vector import Vector
from Circle import Circle
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

class GeometryManager:
    def __init__(self):
        pass
    def VectorsDistance(self, v1 = Vector, v2 = Vector):
        v3 = v1.Sub(v2)
        return v3.Abs()
    # returns true or false weather the vector is inside the circle
    def VectorInCircle(self, v = Vector, c = Circle):
        return self.VectorsDistance(v, c.center) < c.rad