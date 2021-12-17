from emoji import emojize
import random
import time
import os
from playsound import playsound



def clearscreen():
    os.system("clear")

def get_player():
    while True:
        options = "AB"
        bubbles = emojize(":girl:")
        amoeba = emojize(":alien:")
        choose_player = input(f"Choose a character:\n\n{bubbles}Bubbles{bubbles} (B)\n\nor\n\n{amoeba}Amoeba Boys{amoeba} (A)\n\n:")
        choose_player = choose_player.upper()
        if choose_player == "QUIT":
            quit()
        if len(choose_player) !=1 or not choose_player in options:
            print("Invalid input, please type B or A!")
            continue
        if choose_player == "A":
            player = emojize(":alien:")
        else:
            player = emojize(":girl:")
        return player

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for n in range(3):
        row = []
        for i in range(3):
            row.append("  ")
        board.append(row)
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    while True:
        rows = ["A", "B", "C"]
        columns = ["1", "2", "3"]
        player_input = input("Choose a row (A, B, C) and column (1,2,3)!")
        player_input = player_input.upper()
        if player_input == "QUIT":
            quit()
        if len(player_input) != 2 or not player_input[0] in rows \
            or not player_input[1] in columns:
            print("Invalid input, please use A/B/C for rows, and 1/2/3 for columns!")
            continue
        row = rows.index(player_input[0])
        col = columns.index(player_input[1])
        if board[row][col] != "  ":
            print("Cell taken, please try again!")
            continue
        return row, col
    
def switch_player(player):
    if player == emojize(":girl:"):
        next_player = emojize(":alien:")
    else:
        next_player = emojize(":girl:")
    player = next_player
    return player

def can_win(board, player):
    copy_board = board[:]
    for i in range(len(copy_board)):
        for j in range(len(copy_board)):
            if copy_board[i][j] != "  ":
                continue 
            else:
                mark(copy_board, player, i, j)
                if has_won(copy_board, player):
                    return i, j
                else:
                    copy_board[i][j] = "  "

def cell_priority(board):
    corners = [(0, 0), (0,2), (2,0), (2,2)]
    sides = [(0,1), (1,0), (1,2), (2,1)]
    while len(corners) > 0:
        cell = random.choice(corners)
        if board[cell[0]][cell[1]] == "  ":
            return cell 
        corners.remove(cell)
    if board[1][1] == "  ":
        cell = 1,1
        return cell
    while len(sides) > 0:
        cell = random.choice(sides)
        if board[cell[0]][cell[1]] == "  ":
            return cell
        sides.remove(cell)

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    move = can_win(board, player)
    if move != None:
        row, col = move
        return row, col
    else:
        player = switch_player(player)
        move = can_win(board, player)
        if move != None:
            row, col = move
            return row, col
        else:
            move = cell_priority(board)
            row, col = move
            return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player


def has_won(board, player):
    """Returns True if player has won the game."""
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
        if "  " in line:
            num += 1
    if num == 0:
        return True
    else:
        return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders. - FILÓ"""
    letters = "ABC"
    print()
    print("   1     2     3")
    for ind, line in enumerate(board):
        print(letters[ind], end=" ")
        print("  | ".join(line))
        if ind != 2:
            print("  ----+-----+----")
    print()
    

def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 0:
        print("It's a tie!")
    else:
        if winner == emojize(":girl:"):
            print(f"Bubbles{winner} has won!")
            playsound("bubbles_win.mp3")
        else:
            print(f"Amoeba Boys{winner} has won!")



def tictactoe_game():
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    board = init_board()
    mode = choose_mode()
    if mode == "HUMAN-HUMAN":
        player = get_player()
        player = switch_player(player)
        while is_full(board) == False and has_won(board,player) == False:
            print_board(board)
            player = switch_player(player)
            row, col = get_move(board, player)
            mark(board, player, row, col)
            clearscreen()
        print_board(board)
        if has_won(board, player) == True:
            winner = player
        else:
            winner = 0
    elif mode == "AI-HUMAN":
        player = get_player()
        human_player = player
        while is_full(board) == False and has_won(board,player) == False:
            print_board(board)
            player = switch_player(player)
            if human_player == player:
                row, col = get_move(board, player)
            else:
                time.sleep(1)
                row, col = get_ai_move(board, player)
            mark(board, player, row, col)
            clearscreen()
        print_board(board)
        if has_won(board, player) == True:
            winner = player
        else:
            winner = 0
    elif mode == "HUMAN-AI":
        player = get_player()
        human_player = player
        player = switch_player(player)
        while is_full(board) == False and has_won(board,player) == False:
            print_board(board)
            player = switch_player(player)
            if human_player == player:
                row, col = get_move(board, player)
            else:
                time.sleep(1)
                row, col = get_ai_move(board, player)
            mark(board, player, row, col)
            clearscreen()
        print_board(board)
        if has_won(board, player) == True:
            winner = player
        else:
            winner = 0
    elif mode == "AI-AI":
        player = emojize(":alien:")
        player = switch_player(player)
        while is_full(board) == False and has_won(board,player) == False:
            print_board(board)
            player = switch_player(player)
            row, col = get_ai_move(board, player)
            mark(board, player, row, col)
            time.sleep(1)
            clearscreen()
        print_board(board)
        if has_won(board, player) == True:
            winner = player
        else:
            winner = 0
    print_result(winner)    
    return



def choose_mode():
    while True:
        options = "1234"
        playsound("intro.mp3",False)
        choose_mode = input("Choose mode:\n\n1   two-player (HUMAN vs. HUMAN)\n2   one-player (HUMAN vs. AI)\n3   unbeatable machine (AI vs. HUMAN)\n4   AI vs. AI\n")
        choose_mode = choose_mode.upper()
        if choose_mode == "QUIT":
            quit()
        if choose_mode == "" or len(choose_mode) !=1 or not choose_mode in options:
            print("Invalid input, please choose from options 1, 2, 3, or 4!")
            continue
        if choose_mode == "1":
            return "HUMAN-HUMAN"
        elif choose_mode == "2":
            return "HUMAN-AI"
        elif choose_mode == "3":
            return "AI-HUMAN"
        elif choose_mode == "4":
            return "AI-AI"

def main_menu():
    tictactoe_game()

if __name__ == '__main__':
    main_menu()