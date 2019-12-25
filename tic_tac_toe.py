
# Tic Tac Toe for the Command Line
# Author: Xavier Alexander
import os
print("Controls:")
print(f"Top Left - TL\t\t Top Middle - TM \t Top Right - TR")
print(f"Middle Left - ML\t Middle Middle - MM\t Middle Right - MR")
print(f"Bottom Left - BL\t Bottom Middle - BM\t Bottom Right - BR")
print(f"Player 1 = O")
print(f"Player 2 = X")

Player1_letter = 'O'
Player2_letter = 'X'
moves = 0
game_on = True


board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
         'ML': ' ', 'MM': ' ', 'MR': ' ',
         'BL': ' ', 'BM': ' ', 'BR': ' ',
         }


def print_board(board):
    print(f"{board['TL']} | {board['TM']} | {board['TR']}")
    print('--+---+--')
    print(
        f"{board['ML']} | {board['MM']} | {board['MR']}")
    print('--+---+--')
    print(
        f"{board['BL']} | {board['BM']} | {board['BR']}")


def make_move(position, letter):
    board[position] = letter
    print_board(board)


def Player1_win():
    if board['TL'] == 'O' and board['ML'] == 'O' and board['BL'] == 'O' or \
            board['TL'] == 'O' and board['TM'] == 'O' and board['TR'] == 'O' or \
            board['TM'] == 'O' and board['MM'] == 'O' and board['BM'] == 'O' or \
            board['TR'] == 'O' and board['MR'] == 'O' and board['BR'] == 'O' or \
            board['TL'] == 'O' and board['MM'] == 'O' and board['BR'] == 'O' or \
            board['ML'] == 'O' and board['MM'] == 'O' and board['MR'] == 'O' or \
            board['TR'] == 'O' and board['MM'] == 'O' and board['BL'] == 'O' or \
            board['BL'] == 'O' and board['BM'] == 'O' and board['BR'] == 'O':
        return True


def Player2_win():
    if board['TL'] == 'X' and board['ML'] == 'X' and board['BL'] == 'X' or \
            board['TL'] == 'X' and board['TM'] == 'X' and board['TR'] == 'X' or \
            board['TM'] == 'X' and board['MM'] == 'X' and board['BM'] == 'X' or \
            board['TR'] == 'X' and board['MR'] == 'X' and board['BR'] == 'X' or \
            board['TL'] == 'X' and board['MM'] == 'X' and board['BR'] == 'X' or \
            board['ML'] == 'X' and board['MM'] == 'X' and board['MR'] == 'X' or \
            board['TR'] == 'X' and board['MM'] == 'X' and board['BL'] == 'X' or \
            board['BL'] == 'X' and board['BM'] == 'X' and board['BR'] == 'X':
        return True


# def check_game():
#     while True:
#         if Player1_win():
#             print('Player 1, you win')
#             break
#             # global game_on
#             # game_on = False
#         elif Player2_win():
#             print('Player 2, you win')
#             break
#             # game_on = False
#         return game_on


while game_on:
    Player1_pos = input(
        'Player 1, where do you want to make your move? ').upper()
    # os.system('cls' if os.name == 'nt' else 'clear')
    make_move(Player1_pos, Player1_letter)
    if Player1_win():
        print('Player 1, you win!')
        break
    Player2_pos = input(
        'Player 2, where do you want to make your move? ').upper()
    make_move(Player2_pos, Player2_letter)
    if Player2_win():
        print('Player 2, you win!')
        break
else:
    print("Game over")

print(game_on)

# It looks like the global variable game_on is not changing to False 🤔
