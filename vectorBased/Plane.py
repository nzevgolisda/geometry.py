
from Vector import Vector # add all objects, and func from Vector
class Plane:
    def __init__(self, vectors, s, t):
        self.vectors = vectors
        self.v0 = self.vectors[0]
        self.v1 = self.vectors[1]
        self.v2 = self.vectors[2]
        self.n = len(self.vectors)
        self.par = [s, t]
    def param(self): # vector-like object
        e0 = Vector([0, 0])
        e1 = e0.add(self.v0)
        e2 = e1.add(self.v1.multiply(self.par[0]))
        e3 = e2.add(self.v2.multiply(self.par[1]))
        return Vector(e3.list)
    def getPoints(self, n): # list of vectors
        points = []
        for i in range(n+1):
            for j in range(n+1):
                self = Plane(self.vectors, i, j)
                points.append(self.param())
        return points