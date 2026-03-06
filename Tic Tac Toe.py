#Sagi Lugassi
# TicTacToe Project
import random
from operator import index

# נתונים
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player = ["X", "O"]


# הדפסת הלוח
def print_board(board):

    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")


    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")


    print(board[6] + " | " + board[7] + " | " + board[8])

# בדיקת המנצח
def check_winner(board):
    win_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]

    for winCombo in win_combo:
        if board[winCombo[0]] == board[winCombo[1]] == board[winCombo[2]]:
            return True

    return False


# בחירה רנדןמלית של השחקן המתחיל
currentPlayer = random.choice(player)

# הלופ המרכזי ״המנוע״ של המשחק
for i in range(9):
    print_board(board)
# וידוא הזנה של אינפוט תקין
    while True:
        choice = input(f"Player {currentPlayer}: Turn")
        if not choice.isdigit():
            print("ERROR enter a number between 1 and 9")
            continue

        choice = int(choice)
        if choice < 1 or choice > 9:
            print("ERROR enter a number between 1 and 9")
            continue

        index = choice - 1
        if board[index] == "X" or board[index] == "O":
            print("ERROR that spot is taken!")
            continue
        break
# בדיקה אם המערכת זיהתה נצחון
    board[index] = currentPlayer
    if check_winner(board):
     print(f"Player {currentPlayer} wins!")
     break
# אם לא זוהה ניצחון השחקנים מתחלפים והמשחק ממשיך
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
# נגמר המשחק ללא מנצחים
print_board(board)
print("Game Over!")






