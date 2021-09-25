
from Vector import Vector
class Line:
    def __init__(self, vectors, t):
        self.t = t
        self.vectors = vectors
    def param(self):
        v = Vector([0, 0])
        v1 = v.add(self.vectors[0])
        v2 = self.vectors[1].multiply(self.t)
        v3 = v1.add(v2)
        return Vector(v3.list)
    def getPoints(self, n): # list of vectors
        points = []
        for i in range(-n, n, 1):
            self = Line(self.vectors, i)
            points.append(self.param())
        return points