import random

def draw_board():
    for i in board:
        for j in i:
            print(j, end="   ")
        print()

def putting(row, column, x):
    if board[row][column] == "-":
        board[row][column] = x
        return True
    return False

def check_alternative():
    # for horizontal check
    if board[0][0] == board[0][1] == board[0][2] != "-":
        return True
    if board[1][0] == board[1][1] == board[1][2] != "-":
        return True
    if  board[2][0] == board[2][1] == board[2][2] != "-":
        return True

    # for vertical check
    if board[0][0] == board[1][0] == board[2][0] != "-":
        return True
    if board[0][1] == board[1][1] == board[2][1] != "-":
        return True
    if board[0][2] == board[1][2] == board[2][2] != "-":
        return True

    # for diagonal right check
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return True

    # for diagonal left check
    if board[0][2] == board[1][1] == board[2][0] != "-":
        return True

# def check(row, column, x):
#     if board[row][column] == x:

#         # vertical
#         for a in range(4):
#             start = row - a
#             if 0 <= start <= 2:
#                 try:
#                     if (board[start][column] == board[start + 1][column] == board[start + 2][column] == board[start + 3][column] == x):
#                         return True
#                 except IndexError:
#                     pass

#             # horizontal
#             for a in range(4):
#                 start = column - a
#                 if 0 <= start <= 3:
#                     try:
#                         if (board[row][start] == board[row][start + 1] == board[row][start + 2] == board[row][start + 3] == x):
#                             return True
#                     except IndexError:
#                         pass

#             # diagonal right
#             for a in range(4):
#                 startr = row - a
#                 startc = column - a
#                 if 0 <= startr <= 3 and 0 <= startc <= 3:
#                     try:
#                         if (board[startr][startc] == board[startr + 1][startc + 1] == board[startr + 2][startc + 2] == board[startr + 3][startc + 3] == x):
#                             return True
#                     except IndexError:
#                         pass

#             # diagonal left
#             for a in range(4):
#                 startr = row - a
#                 startc = column + a
#                 if 0 <= startr <= 3 and 3 <= startc <= 6:
#                     try:
#                         if (board[startr][startc] == board[startr + 1][startc - 1] == board[startr + 2][startc - 2] == board[startr + 3][startc - 3] == x):
#                             return True
#                     except IndexError:
#                         pass

#             break
#     return False


def draw():
    for row in board:
        for d in row:
            if d == "-":
                return False
    return True

def invalid_move(choose_row, choose_column):
    if choose_row < 0 or choose_row > 2 and choose_column < 0 or choose_column > 2:
        return True
    if board[choose_row][choose_column] != "-":
        return True
    return False

def p1():
    print("1   2   3")
    while True:
        try:
            choose_row = int(input("Choose a row: ")) - 1
            choose_column = int(input("Choose a column: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number among 1 and 3.")
            continue
        if invalid_move(choose_row, choose_column):
            print("Invalid move. Try again.")
            continue
        putting(choose_row, choose_column, "X")
        draw_board()
        return choose_row, choose_column

def p2():
    print("1   2   3")
    while True:
        try:
            choose_row = int(input("Choose a row: ")) - 1
            choose_column = int(input("Choose a column: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number among 1 and 3.")
            continue
        if invalid_move(choose_row, choose_column):
            print("Invalid move. Try again.")
            continue
        putting(choose_row, choose_column, "O")
        draw_board()
        return choose_row, choose_column

def play():
    draw_board()
    while True:
        choose_row, choose_column = p1()
        # if check(choose_row, choose_column, "X"):
        #     print("Player 1 wins!")
        #     break
        if check_alternative():
            print("Player X wins!")
            break
        if draw():
            print("It's a draw!")
            break
        choose_row, choose_column = p2()
        # if check(choose_row, choose_column, "O"):
        #     print("Player 2 wins!")
        #     break
        if check_alternative():
            print("Player O wins!")
            break
        if draw():
            print("It's a draw!")
            break

while True:
    # board = [["-"] * 3 for _ in range(3)]
    board = [["-", "-", "-", "1"], ["-", "-", "-", "2"], ["-", "-", "-", "3"]]
    play()

    answer = input("Do you want to restart the game (y/n): ")
    if answer.lower() != "y":
        print("Thanks for playing!")
        break