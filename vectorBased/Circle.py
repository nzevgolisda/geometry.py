
import math
from Vector import Vector
class Circle:
    def __init__(self, center, r, theta):
        self.center = center
        self.r = r
        self.theta = theta
        self.n = len(self.center.list)
    def param(self): # vector-like object
        v = Vector([0, 0])
        x = self.r*math.cos(self.theta)
        y = self.r*math.sin(self.theta)
        v1 = v.add(self.center.add(Vector([x, y])))
        return Vector(v1.list) #  mporeis na kaneis return v1.list wste na alaxei to getpoints se lista
    def getPoints(self, n): # list of vectors
        points = []
        for i in range(n+1):
            self = Circle(self.center, self.r, 2*i*math.pi/n)
            points.append(self.param())
        return points