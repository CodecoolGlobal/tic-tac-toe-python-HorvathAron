from emoji import emojize


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
    


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders. - FILÓ"""
    a1 = str(board[0][0])
    a2 = str(board[0][1])
    a3 = str(board[0][2])
    b1 = str(board[1][0])
    b2 = str(board[1][1])
    b3 = str(board[1][2])
    c1 = str(board[2][0])
    c2 = str(board[2][1])
    c3 = str(board[2][2])
    board_line1 = ["   1","   2","   3"]
    board_line2 = ["A  ",a1," | ",a2," | ",a3]
    board_line3 = ["  ---+---+---"]
    board_line4 = ["B  ",b1," | ",b2," | ",b3]
    board_line5 = ["  ---+---+---"]
    board_line6 = ["C  ",c1," | ",c2," | ",c3]
    print("".join(board_line1))
    print("".join(board_line2))
    print("".join(board_line3))
    print("".join(board_line4))
    print("".join(board_line5))
    print("".join(board_line6))



def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    # ez egy komment!
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')

if __name__ == '__main__':
    board = init_board()
    player = 1
    print(get_move(board, player))