
import math
class Vector:
    def __init__(self, L):
        self.list = L
        self.n = len(self.list)
    
    def add(self, other):
        L = []
        for i in range(self.n):
            sum = self.list[i] + other.list[i]
            L.append(sum)            
        return Vector(L) # or return L    
    def sub(self, other):
        L = []
        for i in range(self.n):
            sum = self.list[i] - other.list[i]
            L.append(sum)
        return Vector(L) # or return L
    def multiply(self, t):
        L = []
        for i in range(self.n):
            sum = self.list[i] * t
            L.append(sum)
        return Vector(L)
    
    def polar(self):
        r = (self.inn(self)) ** 0.5
        theta1 = math.acos(self.list[0]/r)                # r*math.cos(theta) = self.list[0] = x
        theta2 = math.asin(self.list[1]/r)                # r*math.sin(theta) = self.list[1] = y
        return [r, theta1]   # or Vector([r, theta1])
    def inn(self, other):
        sum = 0
        for i in range(self.n):
            sum += self.list[i] * other.list[i]
        return sum