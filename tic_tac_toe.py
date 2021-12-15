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
    pass



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