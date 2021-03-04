# Tic Tac Toe for the Command Line
# Author: Xavier Alexander

# The welcome screen/message
print("Controls:")
print(f"Top Left - TL\t\t Top Middle - TM \t Top Right - TR")
print(f"Middle Left - ML\t Middle Middle - MM\t Middle Right - MR")
print(f"Bottom Left - BL\t Bottom Middle - BM\t Bottom Right - BR")
print(f"Player 1 = O")
print(f"Player 2 = X")

# Using a dictionary to represent the game board
board = {'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' ',
        }

def print_board(board):
    # Function that prints the board to the screen
    print(f"{board['TL']} | {board['TM']} | {board['TR']}")
    print('--+---+--')
    print(
        f"{board['ML']} | {board['MM']} | {board['MR']}")
    print('--+---+--')
    print(
        f"{board['BL']} | {board['BM']} | {board['BR']}")

def make_move(position, letter):
    # Function that allows players to make moves.
    board[position] = letter
    print_board(board)

def game():
    Player_letter = 'O'
    for i in range(10):
        print(i)
        Player_pos = input(f'Player {Player_letter}, where do you want to make your move? ').upper()

        while Player_pos not in board:
            #Check for valid move
            print('Please make a correct move')
            Player_pos = input(f'Player {Player_letter}, where do you want to make your move? ').upper()

        make_move(Player_pos, Player_letter)
        # Possible moves Player 1 could make that would result in a win.
        if board['TL'] == board['ML'] ==  board['BL'] != ' ' or \
                board['TL'] == board['TM'] == board['TR'] != ' ' or \
                board['TM'] == board['MM'] == board['BM'] != ' ' or \
                board['TR'] == board['MR'] == board['BR'] != ' ' or \
                board['TL'] == board['MM'] == board['BR'] != ' ' or \
                board['ML'] == board['MM'] == board['MR'] != ' ' or \
                board['TR'] == board['MM'] == board['BL'] != ' ' or \
                board['BL'] == board['BM'] == board['BR'] != ' ':
            print(f'Player {Player_letter}, you win!')
            restart()  

        if i == 9:
            restart()
            print('DRAW')

        if Player_letter == 'O':
            Player_letter = 'X'
        else:
            Player_letter = 'O'

def restart():
    choice = input('Would you like to play again??').lower()
    if choice == 'y':
        game()
    elif choice == 'n':
        exit()


if __name__ == "__main__":
    game()
