matrix_1 =[[1,2,3],[4,5,6],[7,8,9]]
matrix_2 =[[1,2,3],[4,5,6],[7,8,9]]

multiply_matrix=[[None]*len(matrix_1) for _ in range(len(matrix_1))]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):
        multiply_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]
print(multiply_matrix)


def isSymmetric(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    if(rows == columns):
        for i in range(rows):
            for j in range(columns):
                if(matrix[i][j]!=matrix[j][i]):
                    return False
                    break
        return True
    


matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]  

print(isSymmetric(matrix))

# 90 degree rows in array
matrix_temp = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]  
matrix_temp_1 = [[None]*3 for _ in range(3)]
for i in range(len(matrix_temp)):
    for j in range(len(matrix_temp[0])):
       matrix_temp_1[j][i] = matrix_temp[i][j]

print(matrix_temp_1)

for row in matrix_temp_1:
    print(row[::-1])

# Flatten array

flatten_arr = []
matrix_arr = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matrix_arr)):
    for j in range(len(matrix_arr[0])):
        flatten_arr.append(matrix_arr[i][j])

print(flatten_arr)


# Reverse rows

matrix_arr = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]

reversed_rows=[[None]*3 for _ in range(3)]

for i in range(len(matrix)):
    reversed_rows[i] = matrix_arr[i][::-1]

print(reversed_rows)

# Reversed 

matrix_arr = [
    [1, 2, 3],
    [4,5,6],
    [7,8,9]
]

reversed_col = [[None]*3 for _ in range(3)]
for i in range(len(matrix_arr)):
    for j in range(len(matrix_arr[0])):
        reversed_col[len(matrix_arr)-i-1][j] = matrix_arr[i][j]
      
print(reversed_col)