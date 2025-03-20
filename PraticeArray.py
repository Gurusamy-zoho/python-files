
################ ARRAY PROBLEMS IN TUTORIAL GATEWAY ######################


# Python Program to Perform Arithmetic Operations on Array

arr_1 = [72,11,54,22,3]
arr_2 = [2,43,0,99,31]
add = []
sub = []
multiple = []
division = []

for i in range(len(arr_1)):
    add.append(arr_1[i] + arr_2[i])
    sub.append(arr_1[i] - arr_2[i])
    multiple.append(arr_1[i] * arr_2[i])
    
    try:
        if arr_2[i] == 0:
            raise ZeroDivisionError("ZeroDivisionError: division by zero")
        division.append(arr_1[i] / arr_2[i])
    except ZeroDivisionError as e:
        print(e)

print(add)
print(sub)
print(multiple)
print(division)

# Python Program to Copy an Array
import numpy as np

inputRange = int(input("Enter range value for numpy array: "))
elements = []

for i in range(inputRange):
    elements.append(int(input(f"Enter element {i + 1}: ")))

Originalarray = np.array(elements)
copyArray = Originalarray

print("Numpy Of Original Array Is:",Originalarray)
print("NumPy Of Copy Array Is :", copyArray)

Python Program to Count Even and Odd Numbers in an Array
import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)

even_count = np.sum(array % 2 == 0)
odd_count = np.sum(array % 2 != 0)
    
print("Count of even number is:",even_count)
print("Count of odd number is:",odd_count)
    
# Python Program to Calculate the Average of an Array

import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
avg = np.mean(array)
print(avg)

# Python Program to Find Array Elements Greater Than Average
import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
avg = np.mean(array)
Greater_than_avg = array[array>avg]
print(f"Array average is {avg} and Greater than avg number is {Greater_than_avg}")


# Python Program to find Largest Number in an Array

import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
largest = np.max(array)

print("Largest value in array: ",largest)

# Python program to Count Positive and Negative Numbers in an Array

import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
count_Positive = np.sum(array>0)
count_Negative = np.sum(array<0)

print("Count of Positive Number is: ",count_Positive)
print("Count of Negative Number is: ",count_Negative)

# Negahon program to find Length of a Numpy Array
import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
Length = len(array)

print("Numpy array of length is: ",Length)


# Python program to find Minimum and Maximum Value in an Array

import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
minVal = np.min(array)
maxVal = np.max(array)

print("Numpy array of min value is: ",minVal)
print("Numpy array of max value is: ",maxVal)

# Python program to Reverse the Numpy Array

import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
reverseArray = array[::-1]
print(reverseArray)

# Python program to find Second Largest in an Array

import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)

Largest = SecondLargest = float('-inf')

for i in range(0,len(array)):
    if(array[i]>Largest):
        SecondLargest = Largest
        Largest = array[i]
    elif(array[i]>SecondLargest and array[i]!=Largest):
        SecondLargest = array[i]
        
print(SecondLargest)
    
# Python program to Print Smallest Number in an Array


import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)

Smallest = float('inf')

for i in range(0,len(array)):

    if(array[i]<Smallest):
        Smallest = array[i]

print("Numpy Array Smallest Number Is: ",Smallest)

# Python program to Sort Array in Ascending Order
List = [78,11,200,65,32]

for i in range(0,len(List)):
    for j in range(0,len(List)-i-1):
        if(List[j]>List[j+1]):
            List[j],List[j+1] = List[j+1],List[j]
print(List)

# Python program to Sort Array in Descending Order
List = [78,11,200,65,32]

for i in range(0,len(List)):
    for j in range(0,len(List)-i-1):
        if(List[j]<List[j+1]):
            List[j],List[j+1] = List[j+1],List[j]
print(List)

# Python program to find Sum of Numpy Array Items
List = [12,234,24,23456,2345]
print(sum(List))

# Python program to find Sum of Even and Odd Numbers in an Array

import numpy as np

RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
sum_Even = np.sum(array[array%2==0])
sum_Odd = np.sum(array[array%2!=0])

print("Sum of Even is: ",sum_Even)
print("Sum of Odd is: ",sum_Odd)

# Python Program to Left Rotate a Numpy Array by n
List = [10, 20, 30, 40, 50]
n = int(input("How many times rotate array: "))

n = n % len(List)
rotated = List[n:] + List[:n]

print(rotated)
# Python Program to Right Rotate a Numpy Array by n

list = [10, 20, 30, 40, 50]
n = int(input("How many times rotate array: "))

n = n % len(list)
rotated = list[-n:] + list[:-n]

print(rotated)






############# Print Array Items ##################

# Python program to Print Even Numbers in an Array

import numpy as np
RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
EvenNumber = array[array%2==0]

print(EvenNumber)

# Python program to Print Odd Numbers in an Array
import numpy as np
RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
EvenNumber = array[array%2!=0]

print(EvenNumber)

# Python program to Print Negative Numbers in an Array

import numpy as np
RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
NegativeNumber = array[array<0]

print(NegativeNumber)

# Python program to Print Array Items
import numpy as np
RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
print(array)

# Python Program to Print Array Elements in Reverse Order
import numpy as np
RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
reversedArray = array[::-1]
print(reversedArray)

# Python Program to Print Array Elements Present on Even Position
import numpy as np
RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
EvenPosition= array[::2]

print(EvenPosition)

# Python Program to Print Array Elements Present on Odd Position
import numpy as np
RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
OddPosition = array[1::2]
print(OddPosition)

# Python program to Print Positive Numbers in an Array

import numpy as np
RangeVal = int(input("Enter a range value: "))
Elements = []

for i in range(0,RangeVal):
    Elements.append(int(input("Enter a elements: ")))
    
array = np.array(Elements)
PostiveNumber = array[array>0]

print(PositiveNumber)

# Python program to Print Unique Items in an Array

size = int(input("Enter the size of the array: "))

elements = []
for i in range(size):
    elements.append(int(input(f"Enter element {i + 1}: ")))

unique_elements = []
for i in elements:
    if i not in unique_elements:
        unique_elements.append(i)

print("Unique elements in the array:", unique_elements)


