  
from math import acos
from cmath import pi
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
from Circle import Circle
from Triangle import Triangle
from Orthogonal import Orthogonal
from GeometryManager import GeometryManager

# Βαση R^2
v0 = Vector(0, 0)
v1 = Vector(1, 0)
v2 = Vector(0, 1)



v3 = Vector(1, 1)
v4 = Vector(1, 5)
v5 = Vector(2, 0)

Ttest1 = Triangle(v0, v1, v2)
Ttest2 = Triangle(v0, v1, v3)
Ttest3 = Triangle(v0, v5, v4)
print(Ttest1.isTrueTriangle())
print(Ttest2.isTrueTriangle())
print(v3.Angle(v1))
print(Ttest1.orthTriangle())
print(Ttest2.orthTriangle())
print(Ttest3.orthTriangle())
print('##############################')
S1 = Orthogonal(v0, v1, v3, v2)
print(S1.isTrueOrth())

print('##############################')

print(v1.linearInd(v2))

v4 = Vector(3, 2)

s1 = v1.Add(v2)
circle1 = Circle(v0, 1)
circle0 = Circle(v2, 0)
print(circle1.distCenter(circle0.center))





v15 = Vector(2, 3)
#v16 = v15.mulBy(-1).Clone()
v16 = v15.mulBy(-1)
v16.printV()


#print('Multiply a Vector: Ok tha to kanw function')
#liakosVector = Vector(1, 2)
#print(liakosVector)
#liakosVector.Multi(-1)
#print(liakosVector)

#def CreateMulti(el):
#    return 2 * el  + 1

#multiplier = CreateMulti(2)
#liakosVector.Multi(multiplier)
#print(liakosVector)

# v3 = v1.Add(v2)
# v4 = v1.Add(v1)

#abs1 = s1.Abs()
#print(abs1)

# int a = 2;
# Unit *u_pointer = new Unit();
# Unit u_value = Unit();
# Unit *u_pointer2 = *u_value;

print("\n|~~~~~~~~~~~~~~~~|\n|Continues|\n|~~~~~~~~~~~~~~~~|\n")
geo = GeometryManager()
point = Vector(0, 0)
circle = Circle(Vector(1,1).Add(Vector(0.1, 0)), 1.42)
print(geo.VectorInCircle(point, circle))