
from Vector import Vector
from Line import Line
from Circle import Circle
from Plane import Plane

# Vectors using lists
e0 = Vector([0, 0])
e1 = Vector([1, 0])
e2 = Vector([0, 1])
#
#e3 = e1.add(e2)
#e4 = e1.sub(e2)
#d0 = e1.inn(e2)
#d1 = e1.inn(e3)
#
## Line using list of vectors and t
# l1 = Line([e0, e1], 2)
# print(l1.param())
# print(l1.getPoints(5))
#
#result = [e3.list, e4.list, d0, d1, l1.param.list]
#print('Your '+str(len(result))+' calculations')
#print('led to '+str(result)+' results.')

# Circle using vector, r and theta
center = e0
c1 = Circle(center, 1, 0)
print(c1.param())
print(c1.getPoints(5))
# 
p1 = Plane([e0, e1, e2], 10, 10)

print('My plane')
print(p1.param().list)
print('points')
print(p1.getPoints(5))