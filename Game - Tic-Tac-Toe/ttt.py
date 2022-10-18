import random


def printBoard(b):
    for i in range(9):
        if i % 3 == 0:
            if i > 0:
                print("")
            print("|", end="")

        print("{}|".format(b[i]), end="")

    print("")


def getUserInput():
    try:
        n = int(input("Enter the position you want to enter X into(1-9): "))
        if n > 0 and n < 10:
            return n - 1
        else:
            return getUserInput()
    except ValueError:
        return getUserInput()


def enterBotInput():
    n = random.randrange(1, 9, 1) - 1
    return n


def WinnerExists(board):
    winner = 0

    for i in range(3):
        if board[3 * i] == board[3 * i + 1] and board[3 * i + 1] == board[3 * i + 2] and board[3 * i] != " ":
            if board[3 * i] == "X":
                winner = 1
                break
            elif board[3 * i] == "O":
                winner = 2
                break
        if board[i] == board[3 + i] and board[3 + i] == board[6 + i] and board[i] != " ":
            if board[i] == "X":
                winner = 1
                break
            elif board[i] == "O":
                winner = 2
                break
    if board[0] == board[4] and board[4] == board[8] and board[0] != " ":
        if board[0] == "X":
            winner = 1
        elif board[0] == "O":
            winner = 2
    if board[2] == board[4] and board[4] == board[6] and board[2] != " ":
        if board[2] == "X":
            winner = 1
        elif board[2] == "O":
            winner = 2

    return winner


def gameSequence():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    used = []

    # printBoard(board)

    for i in range(9):
        if i % 2 == 0:
            printBoard(board)

        winner = WinnerExists(board)

        if winner > 0:
            break

        if i % 2 == 0:
            n = getUserInput()

            while n in used:
                print("{} has already been occupied!".format(n))
                n = getUserInput()

            used.append(n)
            board[n] = "X"
        else:
            n = enterBotInput()

            while n in used:
                n = enterBotInput()

            used.append(n)
            board[n] = "O"

    if len(used) == 9:
        printBoard(board)

    winner = WinnerExists(board)

    if winner > 0:
        if winner == 1:
            print("You won!!!!")
        else:
            print("You lost!!!!")
    else:
        print("It's a draw!!!")

    choice = input("Do you want to play again(Y/N): ")

    if choice == "Y" or choice == "y" or choice == "yes":
        gameSequence()
    else:
        return


if __name__ == "__main__":
    gameSequence()
