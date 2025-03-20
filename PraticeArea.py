# Python Program to find the Area of a Circle

import math
radius = int(input("Enter a radius value in cm: "))
pi = math.pi
area = 22/7*pi*radius
print("Area of a Circle is: ",area)

# Python Program to find Diameter, Circumference, and Area Of a Circle

import math
pi = math.pi

radius = float(input("Enter a radius value in cm: "))
Diameter = 2*radius
Circumference = 2*pi*radius

print("Diameter of a circle is:",Diameter)
print("Circumference of a circle is:",Circumference)

# Python Program to find Equilateral Triangle Area

import math
side = float(input("Enter a equilateral triangle side value: "))
areaOfTriangle = (math.sqrt(3)/4)*(math.pow(side,2))

print("The area of equilateral triangle is: ",areaOfTriangle)


# Python Program to check Triangle is Valid or Not

sideOfA = float(input("Enter a side value: "))
sideOfB = float(input("Enter b side value: "))
sideOfC = float(input("Enter c side value: "))

if(((sideOfA+sideOfB)>sideOfC) and ((sideOfB+sideOfC)>sideOfA) and ((sideOfA+sideOfC)>sideOfB)):
    print("This is a valid triangle")
else:
    print("This is a invalid triangle")

# Python Program to Find angle of a Triangle if two angles are given

Angle_1 = int(input("Enter a first angle: "))
Angle_2 = int(input("Enter a second angle: "))

Angle_3 = 180-(Angle_1+Angle_2)
print("Third angle is: ",Angle_3)

# Python Program for Isosceles Triangle Area

import math
side = float(input("Enter a side value: "))
base = float(input("Enter a base value: "))

Area = (base*math.sqrt((4*(math.pow(side,2)))-math.pow(base,2))) / 4
print("Area of Isosceles triangle is:",Area)

# Python Program for Triangle Area
import math

a = float(input("Enter a side: "))
b = float(input("Enter a another side: "))
c = float(input("Enter a last side: "))

s = (a+b+c)/2
Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Triangle of area is: ",Area)

# Python program to find Triangle area using base and height
b = float(input("Enter breath side: "))
h = float(input("Enter a height side: "))
Area = 1/2*b*h
print("Area of triangle is:",Area)

# Python program to find Area of a Trapezoid


a = float(input("Enter a side: "))
b = float(input("Enter a another side: "))
h = float(input("Enter a height side: "))

Area = 1/2*((a+b)*h)
print("Trapezoid of area is: ",Area)

# Python Program for Parallelogram Area

b = float(input("Enter a breath side: "))
h = float(input("Enter a height side: "))
A=b*h
print("Parallelogram area is:",A)

# Python program to find Rectangle Area using length and width

length = float(input("Enter a length value: "))
width = float(input("Enter a width value: "))

AreaOfTriangle = length*width
print("Area of Triangle is:",AreaOfTriangle)

# Python program to find Rectangle Perimeter using length and width

length = float(input("Enter a length value: "))
width = float(input("Enter a width value: "))

Perimeter = length*width
print("Perimeter of triangle is: ",Perimeter)

# Python program for Rhombus Area

d1 = float(input("Enter a first diagonal value: "))
d2 = float(input("Enter a second diagonal value: "))

Area = (d1*d2)/2
print("Area of Rhombus: ",Area)

# Python program for Rhombus Perimeter

a = float(input("Enter a length of side: "))
perimeter = 4*a
print("Perimeter od Rhombus is: ",perimeter)