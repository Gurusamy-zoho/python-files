# Using List

matrix = [[0 for _ in range(3)]for i in range(3)]

print(matrix)

# Use Numpy Array

import numpy as np

matrixArray = np.zeros((3,3),dtype=int)
print(matrixArray)

# Using List

identityMatrix = [[1 if i==j else 0 for j in range(3)]for i in range(3)]
print(identityMatrix)

# Use Numpy Array

identityArray = np.eye(3,dtype=int)
print(identityArray)

# Find numper of Rows & Columns in 2D Array

Matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
rows = len(Matrix)
columns = len(matrix[0])

print("Number of rows in matrix: ",rows)
print("Number of columns in matrix: ",columns)

# Print 2D Array to Matrix

ArrMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in ArrMatrix:
    print(" ".join(map(str,row)))
    
# Sum of all elements in matrix array

sumMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sumOfAllElements = 0
for rows in range(0,len(sumMatrix)):
    for columns in range(0,len(sumMatrix[rows])):
        sumOfAllElements+=sumMatrix[rows][columns]
        
print(sumOfAllElements)

# Find Maximum and Minimum value of matrix

maxminMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

max_value = maxminMatrix[0][0]
min_value = maxminMatrix[0][0]

for rows in maxminMatrix:
    for columns in rows:
        if columns > max_value:
            max_value = columns
        if columns < min_value:
            min_value = columns

print("Maximum value of 2D Matrix",max_value)
print("Minimum value of 2D Matrix",min_value)
        
        
# Find sum of each row

sumOfEachRowMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sumOfEachRow = 0
for i in range (len(sumOfEachRowMatrix)):
    sumOfEachRow = sum(sumOfEachRowMatrix[i])
    print(f"Sum of {i} row in matrix: {sumOfEachRow}")

# Find sum of each row in Numpy Array

import numpy as np
sumOfEachRowArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr = np.array(sumOfEachRowArray)
print(np.sum(arr,axis=1))

# Find sum of each column 

sumOfEachColumnMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
columns = len(sumOfEachColumnMatrix[0])
for col in range(columns):
    sumOfEachCol = sum(row[col] for row in sumOfEachColumnMatrix)
    print(f"Sum of column {col}: { sumOfEachCol}")
    
# Find sum of each Column in Numpy Array

import numpy as np
sumOfEachColArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

arr = np.array(sumOfEachColArray)
print(np.sum(arr,axis=0)) 

# Find index of maximum element in 2D Array

maxArray = [[91, 29, 3], [40, 235, 16], [7, 83, 12]]

max_value = maxArray[0][0]
rowIndex = 0
colIndex = 0
for i in range (len(maxArray)):
    for j in range(len(maxArray[i])):
        if maxArray[i][j] > max_value:
            max_value=maxArray[i][j]
            rowIndex = i
            colIndex = j
print(f"The maximum value {max_value} element of row index is: ({i},{j})")

# Transpose matrix

transposeMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(transposeMatrix)
cols = len(transposeMatrix[0])
transposed = [[0] * rows for _ in range(cols)]
for i in range(len(transposeMatrix)):
    for j in range(len(transposeMatrix[i])):
        transposed[j][i] = transposeMatrix[i][j]
print(transposed)

# Lower Intermediate Level:

#     Multiply two 2D arrays (matrices) of compatible sizes.

#     Check if a given 2D array is symmetric.

#     Rotate a 2D array 90 degrees clockwise.

#     Flatten a 2D array into a 1D list.

#     Reverse all rows of a 2D array.

#     Reverse all columns of a 2D array.

#     Check if a given 2D array is a square matrix.

#     Create a spiral matrix of size NxN (e.g., for N=3, output: [[1,2,3],[8,9,4],[7,6,5]]).

#     Compute the row-wise and column-wise mean of a 2D array.

#     Swap two specific rows in a 2D array.



# Intermediate Level:

#     Find the diagonal sum of a square 2D array.

#     Rotate a 2D array 180 degrees.

#     Remove duplicate rows from a 2D array.

#     Implement Conway's Game of Life for one iteration.

#     Find the saddle point of a 2D array (an element that is the minimum in its row and maximum in its column, or vice versa).