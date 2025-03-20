# Volume and Surface Area of a Sphere
import math
r = float(input("Enter a radius in cm: "))
pi = math.pi

Volume = 4/3*pi*math.pow(r,3)
Area = 4*pi*math.pow(r,2)

print(f"Volume and Surface Area of a Sphare is {Volume},{Area}")

# Volume and Surface Area of a Cylinder

import math
pi = math.pi

r = float(input("Enter a radius value in cm: "))
h = float(input("Enter a height value in cm: "))

SurfaceArea = 2*pi*r*h + 2*pi*r
Volume = pi*math.pow(r,2)*h

print("Surface Area of Cylinder is: ",SurfaceArea)
print("Volume of Cyclinder is: ",Volume)

# Volume and Surface Area of a Cube

import math
a = float(input("Enter a side value: "))
SurfaceArea = 6*a
Volume = math.pow(a,3)

print("Surface Area of Cube is: ",SurfaceArea)
print("Volume of Cube is: ",Volume)

# Volume and Surface Area of a Cone

import math
pi = math.pi

r = float(input("Enter a radius value: "))
l = float(input("Enter a length value: "))
h = float(input("Enter a height value: "))
SurfaceArea = pi*r*l + pi*math.pow(r,2)
Volume = 1/3*pi*math.pow(r,2)*h

print("Surface Area of Cone is: ",SurfaceArea)
print("Volume of Cone is: ",Volume)


# Volume and Surface Area of a Cuboid

w = float(input("Enter a width value: "))
l = float(input("Enter a length value: "))
h = float(input("Enter a height value: "))

Volume = w * l * h
SurfaceArea = 2 * (l * w + w * h + h * l)

print("Surface Area of Cuboid is:", SurfaceArea)
print("Volume of Cuboid is:", Volume)
