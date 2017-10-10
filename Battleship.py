# Single player console based battleship
# Coded by Sabbir Ahmed Shibli
# An open source project

from random import randint      # importing random generating function

# Initializing 5x5 matrix for game board
board = []
for i in range(5):
    board.append(['O'] * 5)


# printing the matrix board
def print_board(board):
    for row in board:
        s = ' '.join(row)
        print(s)


# generating random row
def random_row(board):
    return randint(0, 4)


# generating random column
def random_column(board):
    return randint(0, 4)


# Input/Output and result generator function
def io_n_result():
    for turn in range(1, 5):
        # Taking input of guessed row and column
        print("Turn ", turn, ":")
        row_input = int(input("Enter the row: "))
        column_input = int(input("Enter the column: "))

        # Condition for winning
        if row_input == correct_row and column_input == correct_column:
            print("Yes! Yes! You hit the correct place! :)")
            break
        # Condition for all loses
        else:
            # Checking whether input is in the range of matrix board
            if row_input not in range(5) or column_input not in range(5):
                print("Hei! You hit outside of the sea! :/")
            # Checking about previous hit
            elif board[row_input][column_input] == "X":
                print("You have hit here before! Try another.")
            # Checking further conditions and setting last input in the matrix
            else:
                print("Oh! You missed the right place! :(")
                board[row_input][column_input] = "X"
                print_board(board)
        # If user crossed 4 turns then game is over
        if turn == 4:
            print("Game Over!")


print_board(board)                      # Calling board printing function
correct_row = random_row(board)         # Calling random row generator function
correct_column = random_column(board)   # Calling random column generator function

# print(correct_row)                    # Printing random row number
# print(correct_column)                 # Printing random column number

io_n_result()                           # Calling i/o and result function
