"""
Name: Scarlett Duncan
lab9.py

Problem: Write a code that creates a playable game of tic-tac-toe

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if str(position).isnumeric():
        return True
    else:
        return False


def fill_spot(board, position, character):
    character = character.strip()
    character = character.lower()
    board[position - 1] = character


def game_is_won(board):
    if (board[4] == board[2] == board[6]) or (board[4] == board[0] == board[8]):
        return True
    elif (board[0] == board[1] == board[2]) or (board[0] == board[3] == board[6]):
        return True
    elif (board[4] == board[3] == board[5]) or (board[4] == board[1] == board[7]):
        return True
    elif (board[8] == board[2] == board[5]) or (board[8] == board[6] == board[7]):
        return True
    else:
        return False


def game_over(board):
    if game_is_won(board):
        return True
    else:
        num = True
        acc_i = 0
        if num or acc_i <= len(board):
            for i in range(len(board)):
                num = str(board[i]).isnumeric()
                if num:
                    return False
        else:
            return True


def get_winner(board):
    if game_is_won(board):
        if (board[4] == board[2] == board[6]) or (board[4] == board[0] == board[8]):
            return board[4]
        elif (board[0] == board[1] == board[2]) or (board[0] == board[3] == board[6]):
            return board[0]
        elif (board[4] == board[3] == board[5]) or (board[4] == board[1] == board[7]):
            return board[4]
        elif (board[8] == board[2] == board[5]) or (board[8] == board[6] == board[7]):
            return board[8]
        else:
            return None
    elif game_over():
        return None


def play(board):
    ans = "Yes"
    shape_x = "x"
    shape_o = "o"
    while ans[0].lower() == 'y':
        while not game_over(board):
            print_board(board)
            position_x = eval(input("X's, choose a position:"))
            if is_legal(board, position_x):
                fill_spot(board, position_x, shape_x)
            else:
                print("Choose a different position")

            print_board(board)
            if not game_over(board):
                position_y = eval(input("O's, choose a position:"))
                if is_legal(board, position_y):
                    fill_spot(board, position_y, shape_o)
                else:
                    print("choose a different position")

        if get_winner(board) == "x":
            print("X's win!")
        elif get_winner(board) == "o":
            print("O's win!")
        else:
            print("Tie")
        ans = input("Do you want to keep playing?")
        board = build_board()




def main():
    board = build_board()
    play(board)


if __name__ == '__main__':
    main()
