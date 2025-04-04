# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# for i in range(len(matrix)):
#     print(matrix[i])

# sum = 0

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         sum+=matrix[i][j]

# print("Sum of all elements is: ",sum)

# even_count = 0
# odd_count = 0


# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] % 2 == 0:
#             even_count+=1
#         else:
#             odd_count+=1

# print("Count odd numbers: ",odd_count)
# print("Count even number is: ",even_count)

# max_value = matrix[0][0]
# min_value = matrix[0][0]


# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] > max_value:
#             max_value = matrix[i][j]
#         if matrix[i][j] < min_value:
#             min_value = matrix[i][j]
# print("Maximum value of 2D array is: ",max_value)
# print("Minimum value of 2D array is: ",min_value)


# temp = [[None]*3 for _ in range(3)]

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         temp[j][i] = matrix[i][j]

# print(temp)

# matrix_1 = [
#     [1, 2, 3],
#     [2, 5, 6],
#     [3, 6, 9]
# ]

# def is_symmetric(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] != matrix[j][i]:
#                return False
#     return True

# print(is_symmetric(matrix_1))


# sum = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i == j:
#             sum+= matrix[i][j]

# print("Sum of main diagonal matrix is: ",sum)

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if i>=j:
#             print(matrix[i][j])


# # dict = {}

# # for i in range(len(matrix)):
# #     sum_Row = 0
# #     for j in range(len(matrix[i])):
# #        sum_Row+=matrix[i][j]
# #     dict[i] = sum_Row

# # max_key = None
# # max_value = float('-inf')

# # for key in dict:
# #     if dict[key] > max_value:
# #         max_value = dict[key]
# #         max_key = key

# # print("Key with max value:", max_key)


# # for i in range(len(matrix)):
# #     for j in range(len(matrix)-i-1):
# #         if matrix[j] > matrix[j+1]:
# #            matrix[j],matrix[j+1] = matrix[j+1],matrix[j]


# # for i in range(len(matrix)):
# #    print(matrix[i])


# def display_grid(grid, player_pos):
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if (i, j) == player_pos:
#                 print('P', end=' ')
#             elif grid[i][j] == 'G':
#                 print('G', end=' ')
#             else:
#                 print('.', end=' ')
#         print()
#     print()

# def move_player(command, pos, rows, cols):
#     i, j = pos
#     if command == 'W' and i > 0:
#         i -= 1
#     elif command == 'S' and i < rows - 1:
#         i += 1
#     elif command == 'A' and j > 0:
#         j -= 1
#     elif command == 'D' and j < cols - 1:
#         j += 1
#     return (i, j)

# # Initialize game
# rows, cols = 5, 5
# grid = [['.' for _ in range(cols)] for _ in range(rows)]
# player_pos = (0, 0)
# goal_pos = (4, 4)
# grid[goal_pos[0]][goal_pos[1]] = 'G'

# print("🎮 Welcome to the Grid Game!")
# print("Controls: W = Up, A = Left, S = Down, D = Right")
# print("Goal: Reach the 'G' tile!")

# while True:
#     display_grid(grid, player_pos)
    
#     if player_pos == goal_pos:
#         print("🎉 You reached the goal! You win!")
#         break

#     command = input("Move (W/A/S/D): ").upper()
#     if command in ['W', 'A', 'S', 'D']:
#         player_pos = move_player(command, player_pos, rows, cols)
#     else:
#         print("❌ Invalid input. Please enter only W, A, S, or D.")


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check main diagonal
    if all(board[i][i] == player for i in range(3)):
        return True

    # Check secondary diagonal
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

print("🎮 Welcome to Tic-Tac-Toe!")

while True:
    print_board(board)
    print(f"Player {current_player}'s turn.")

    try:
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if board[row][col] != " ":
            print("❗Cell already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🏆 Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    except (ValueError, IndexError):
        print("❌ Invalid input. Please enter numbers between 0 and 2.")
