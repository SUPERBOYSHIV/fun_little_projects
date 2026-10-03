board = [["-"] * 7 for u in range(6)]
def draw_board():
    for i in board:
        for j in i:
            print(j, end="   ")
        print()

def dropping(cc, x):
    for v in range(5, -1, -1):
        if board[v][cc] == "-":
            board[v][cc] = x
            break

def check():
    for a in range(6):
        for b in range(4):
            if board[a][b] == board[a][b + 1] == board[a][b + 2] == board[a][b + 3] != "-":
                return True

    for a in range(3):
        for b in range(7):
            if board[a][b] == board[a + 1][b] == board[a + 2][b] == board[a + 3][b] != "-":
                return True

    for a in range(3):
        for b in range(4):
            if board[a][b] == board[a + 1][b + 1] == board[a + 2][b + 2] == board[a + 3][b + 3] != "-":
                return True

    for a in range(3):
        for b in range(3, 7):
            if board[a][b] == board[a + 1][b - 1] == board[a + 2][b - 2] == board[a + 3][b - 3] != "-":
                return True

def draw():
    for d in board[0]:
        if d == "-":
            return False
        return True

def invalid_move(cc):
    if cc < 0 or cc > 6:
        return True
    if board[0][cc] != "-":
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
        break

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
        break

def play():
    draw_board()
    while True:
        p1()
        if check():
            print("Player 0 wins!")
            break
        if draw():
            print("It's a draw!")
            break
        p2()
        if check():
            print("Player O wins!")
            break
        if draw():
            print("It's a draw!")
            break

play()