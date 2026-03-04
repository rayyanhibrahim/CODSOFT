import math

# Create board
board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Game Loop
print("TIC-TAC-TOE GAME")
print("You are X, AI is O")

while True:
    print_board()
    
    # Human move
    position = int(input("Enter position (1-9): ")) - 1
    if board[position] == " ":
        board[position] = "X"
    else:
        print("Invalid move!")
        continue

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

    # AI move
    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if is_draw():
        print_board()
        print("It's a Draw!")
        break

#output
TIC-TAC-TOE GAME
You are X, AI is O

  |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Enter position (1-9): 5

  |   |  
--+---+--
  | X |  
--+---+--
  |   | O

Enter position (1-9): 1
...
AI Wins!
