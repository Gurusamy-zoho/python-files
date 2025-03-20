
# ARRAY PROBLEMS IN TUTORIAL GATEWAY


# # Python Program to Perform Arithmetic Operations on Array

# arr_1 = [72,11,54,22,3]
# arr_2 = [2,43,0,99,31]
# add = []
# sub = []
# multiple = []
# division = []

# for i in range(len(arr_1)):
#     add.append(arr_1[i] + arr_2[i])
#     sub.append(arr_1[i] - arr_2[i])
#     multiple.append(arr_1[i] * arr_2[i])
    
#     try:
#         if arr_2[i] == 0:
#             raise ZeroDivisionError("ZeroDivisionError: division by zero")
#         division.append(arr_1[i] / arr_2[i])
#     except ZeroDivisionError as e:
#         print(e)

# print(add)
# print(sub)
# print(multiple)
# print(division)

# # Python Program to Copy an Array
# import numpy as np

# inputRange = int(input("Enter range value for numpy array: "))
# elements = []

# for i in range(inputRange):
#     elements.append(int(input(f"Enter element {i + 1}: ")))

# Originalarray = np.array(elements)
# copyArray = Originalarray

# print("Numpy Of Original Array Is:",Originalarray)
# print("NumPy Of Copy Array Is :", copyArray)

# Python Program to Count Even and Odd Numbers in an Array
# import numpy as np

# RangeVal = int(input("Enter a range value: "))
# Elements = []

# for i in range(0,RangeVal):
#     Elements.append(int(input("Enter a elements: ")))
    
# array = np.array(Elements)

# even_count = np.sum(array % 2 == 0)
# odd_count = np.sum(array % 2 != 0)
    
# print("Count of even number is:",even_count)
# print("Count of odd number is:",odd_count)
    
## Python Program to Calculate the Average of an Array

# import numpy as np

# RangeVal = int(input("Enter a range value: "))
# Elements = []

# for i in range(0,RangeVal):
#     Elements.append(int(input("Enter a elements: ")))
    
# array = np.array(Elements)
# avg = np.mean(array)
# print(avg)

## Python Program to Find Array Elements Greater Than Average
# import numpy as np

# RangeVal = int(input("Enter a range value: "))
# Elements = []

# for i in range(0,RangeVal):
#     Elements.append(int(input("Enter a elements: ")))
    
# array = np.array(Elements)
# avg = np.mean(array)
# Greater_than_avg = array[array>avg]
# print(f"Array average is {avg} and Greater than avg number is {Greater_than_avg}")


# Python Program to find Largest Number in an Array
# Python program to Count Positive and Negative Numbers in an Array
# Python program to find Length of a Numpy Array
# Python program to find Minimum and Maximum Value in an Array
# Python program to Reverse the Numpy Array
# Python program to find Second Largest in an Array
# Python program to Print Smallest Number in an Array
# Python program to Sort Array in Ascending Order
# Python program to Sort Array in Descending Order
# Python program to find Sum of Numpy Array Items
# Python program to find Sum of Even and Odd Numbers in an Array
# Python Program to Left Rotate a Numpy Array by n
# Python Program to Right Rotate a Numpy Array by n






