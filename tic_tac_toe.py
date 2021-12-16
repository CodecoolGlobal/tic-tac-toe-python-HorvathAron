#from emoji import emojize

def get_player():
    while True:
        options = "AB"
        choose_player = input("Choose a character: Bubbles emoji (B) or Amoeba Boys emoji (A): ")
        choose_player = choose_player.upper()
        if len(choose_player) !=1 or not choose_player in options:
            print("Invalid input, please type B or A")
            continue
        if choose_player == "A":
            player = "O"
        else:
            player = "X"
        return player

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for n in range(3):
        row = []
        for i in range(3):
            row.append(".")
        board.append(row)
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    while True:
        rows = ["A", "B", "C"]
        columns = ["1", "2", "3"]
        player_input = input("Choose a row (A, B, C) and column (1,2,3)!")
        player_input = player_input.upper()
        if len(player_input) != 2 or not player_input[0] in rows \
            or not player_input[1] in columns:
            print("Invalid input, use a letter-number combo in range A-B-C 1-2-3")
            continue
        row = rows.index(player_input[0])
        col = columns.index(player_input[1])
        if board[row][col] != ".":
            print("Cell taken, pls try again")
            continue
        return row, col
    
def switch_player(player):
    if player == "X":
        next_player = "O"
    else:
        next_player = "X"
    player = next_player
    return player

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player


def has_won(board, player):
    """Returns True if player has won the game."""
    board[0][0]
    if "".join(board[0]) == (player * 3) or "".join(board[1]) == (player * 3) or "".join(board[2]) == (player * 3):
        return True
    elif "".join(board[0][0] + board[1][0] + board[2][0]) == (player * 3) or "".join(board[0][1] + board[1][1] + board[2][1]) == (player * 3) or "".join(board[0][2] + board[1][2] + board[2][2]) == (player * 3):
        return True
    elif "".join(board[0][0] + board[1][1] + board[2][2]) == (player * 3) or "".join(board[0][2] + board[1][1] + board[2][0]) == (player * 3):
        return True
    else:
        return False


def is_full(board):
    """Returns True if board is full."""
    num = 0
    for line in board:
        if "." in line:
            num += 1
    if num == 0:
        return True
    else:
        return False
    #if "." == (board[0][0] or board[0][1] or board[0][2] or board[1][0] or board[1][1] or board[1][2] or board[2][0] or board[2][1] or board[2][2]):
        #return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders. - FILÓ"""
    letters = "ABC"
    print()
    print("   1   2   3")
    for ind, line in enumerate(board):
        print(letters[ind], end="  ")
        print(" | ".join(line))
        if ind != 2:
            print("  ---+---+---")
    print()
    

def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print("GAME OVER")
    else:
        print(f"Congrats {winner}, you win!")



def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    player = get_player()
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    # ez egy komment!
    while is_full(board) == False and has_won(board,player) == False:
        print_board(board)
        player = switch_player(player)
        row, col = get_move(board, player)
        mark(board, player, row, col)
    print_board(board)
    if has_won(board, player) == True:
        winner = player
    else:
        winner = 0
    print_result(winner)
    return

def main_menu():
    tictactoe_game('HUMAN-HUMAN')

if __name__ == '__main__':
    main_menu()