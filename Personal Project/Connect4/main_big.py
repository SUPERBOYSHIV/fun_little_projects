import random

def draw_board():
    for i in board:
        for j in i:
            print(j, end="   ")
        print()

def dropping(column, x):
    for row in range(5, -1, -1):
        if board[row][column] == "-":
            board[row][column] = x
            break

# def check_alternative():
#     # for horizontal check
#     for row in range(6):
#         for column in range(4):
#             if board[row][column] == board[row][column + 1] == board[row][column + 2] == board[row][column + 3] != "-":
#                 return True

#     # for vertical check
#     for row in range(3):
#         for column in range(7):
#             if board[row][column] == board[row + 1][column] == board[row + 2][column] == board[row + 3][column] != "-":
#                 return True

#     # for diagonal right check
#     for row in range(3):
#         for column in range(4):
#             if board[row][column] == board[row + 1][column + 1] == board[row + 2][column + 2] == board[row + 3][column + 3] != "-":
#                 return True

#     # for diagonal left check
#     for row in range(3):
#         for column in range(3, 7):
#             if board[row][column] == board[row + 1][column - 1] == board[row + 2][column - 2] == board[row + 3][column - 3] != "-":
#                 return True

def check(column, x):
    for row in range(6):
        if board[row][column] == x:

            # vertical
            for a in range(4):
                start = row - a
                if 0 <= start <= 2:
                    try:
                        if (board[start][column] == board[start + 1][column] == board[start + 2][column] == board[start + 3][column] == x):
                            return True
                    except IndexError:
                        pass

            # horizontal
            for a in range(4):
                start = column - a
                if 0 <= start <= 3:
                    try:
                        if (board[row][start] == board[row][start + 1] == board[row][start + 2] == board[row][start + 3] == x):
                            return True
                    except IndexError:
                        pass

            # diagonal right
            for a in range(4):
                startr = row - a
                startc = column - a
                if 0 <= startr <= 3 and 0 <= startc <= 3:
                    try:
                        if (board[startr][startc] == board[startr + 1][startc + 1] == board[startr + 2][startc + 2] == board[startr + 3][startc + 3] == x):
                            return True
                    except IndexError:
                        pass

            # diagonal left
            for a in range(4):
                startr = row - a
                startc = column + a
                if 0 <= startr <= 3 and 3 <= startc <= 6:
                    try:
                        if (board[startr][startc] == board[startr + 1][startc - 1] == board[startr + 2][startc - 2] == board[startr + 3][startc - 3] == x):
                            return True
                    except IndexError:
                        pass

            break
    return False


def draw():
    for d in board[0]:
        if d == "-":
            return False
    return True

def invalid_move(choose_column):
    if choose_column < 0 or choose_column > 6:
        return True
    if board[0][choose_column] != "-":
        return True
    return False

def p1():
    print("1   2   3   4   5   6   7")
    while True:
        try:
            choose_column = int(input("Choose a column: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number among 1 and 7.")
            continue
        if invalid_move(choose_column):
            print("Invalid move. Try again.")
            continue
        dropping(choose_column, "0")
        draw_board()
        return choose_column

def p2():
    print("1   2   3   4   5   6   7")
    while True:
        try:
            choose_column = int(input("Choose a column: ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number among 1 and 7.")
            continue
        if invalid_move(choose_column):
            print("Invalid move. Try again.")
            continue
        dropping(choose_column, "O")
        draw_board()
        return choose_column

def play():
    draw_board()
    while True:
        choose_column = p1()
        if check(choose_column, "0"):
            print("Player 1 wins!")
            break
        # if check_alternative():
        #     print("Player 0 wins!")
        #     break
        if draw():
            print("It's a draw!")
            break
        choose_column = p2()
        if check(choose_column, "O"):
                    print("Player 2 wins!")
                    break
        # if check_alternative():
        #     print("Player O wins!")
        #     break
        if draw():
            print("It's a draw!")
            break

while True:
    board = [["-"] * 7 for _ in range(6)]
    play()

    answer = input("Do you want to restart the game (y/n): ")
    if answer.lower() != "y":
        print("Thanks for playing!")
        break