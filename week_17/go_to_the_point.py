```
Like in the lecture, define a class called Point. However, it should be a 3D-Point, with coordinates x, y, and z.
Define an appropriate class with constructor, equality, and string representation. You should be able to
create a list of points like l = [Point(1,2,3), Point(0,0,0)]. Print each element of the list. Check that
Point(1, 2, 3) == Point(1, 2, 3).
Implement the methods largest(), norm(), and cross_product(q). The first should return the largest
component, e.g. Point(-10, 2, 8).largest() returns 8. The second computes the (Euclidean) norm
of the point, e.g. Point(1, 1, 1).norm() should be the the square-root of 3. The third computes the
cross product of two 3D points. Note: The cross product of two points aand bis a third point cwhere
cx= aybz≠azby, cy= azbx≠axbz, and cz= axby≠aybx.
Next, we want to define some magic methods for this class. Concretely, the absolute value should return
the norm of the point (__abs__). Additionally, adding two points (__add__) should create the summed
point and multiplying (__mul__) with a number returns the scaled point (every component is multiplied
with the number).
Create a set of points. Recall what you need to implement to allow objects to be added to a set.
```


class Point:
  def __init__(self, x, y, z):
  self.x, self.y, self.z = x, y, z
  def largest(self):
  return max(self.as_tuple())
  
  def norm(self):
  return sum(c**2 for c in self.as_tuple()) ** 0.5
  
  def cross_product(self, other):
    x = self.y * other.z - self.z * other.y
    y = self.z * other.x - self.x * other.z
    z = self.x * other.y - self.y * other.x
    return Point(x, y, z)
  
  def as_tuple(self):
    return (self.x, self.y, self.z)
  
  def __abs__(self):
    return self.norm()
  
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y, self.z + other.z)
  
  def __mul__(self, other):
    if isinstance(other, float) or isinstance(other, int):
      return Point(other * self.x, other * self.y, other * self.z)
    raise NotImplementedError
  
  def __rmul__(self, other):
    return self * other
  
  def __str__(self):
    return f"({self.x},{self.y},{self.z})"
  
  def __eq__(self, other):
    # return isinstance(other, Point) and self.x == other.x and self.y == other.y and self.z == other.zÒæ
    return isinstance(other, Point) and self.as_tuple() == other.as_tuple()
    
  def __hash__(self):
    return hash(self.as_tuple() 

points = [Point(1, 2, 3), Point(0, 0, 0)]
print("List")
for p in points:
  print(f"{p} has norm {abs(p)}")
print()
a = Point(1, 2, 3)
b = Point(2, -1, 3)
print(f"Cross: {a} x {b} = {a.cross_product(b)}")
print()
print("Points equal:", Point(1, 2, 3) == Point(1, 2, 3))
print()

p = Point(1, -1, 0)
print(f"{p} times 2.5 is {p * 2.5}")
print()
s = {Point(1, 2, 3), Point(1, 2, 3), p}
print(f"Set has size {len(s)}")




                  
