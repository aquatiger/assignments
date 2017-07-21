import random


class Player:
    def __init__(self, name, location_i, location_j):
        self.name = name
        self.location_i = location_i
        self.location_j = location_j

def print_board(board, player):
    for j in range(len(board)):
        for i in range(len(board[j])):
            if player.location_i == i and player.location_j == j:
                print('X', end=' ')
            else:
                print(board[i][j], end=' ')
        print()

width = 10
height = 10
board = [[0 for j in range(height)] for i in range(width)]

for i in range(len(board[0])):
    board[0][i] = '*'

for j in range(len(board[0])):
    board[j][len([j])-1] = 'l'

player = Player('Link', 0, 0)

for k in range(10):
    i = random.randint(0, width-1)
    j = random.randint(0, height-1)
    board[0] = '\u058D'
    board[i][j] = 'X'

def check_location(board, player):
    if board[player.location_i][player.location_j] == 'X':
        print('You have encountered an orc!!!')
        action = input('what do you do? ')
        if action == 'attack':
            print('You have slain the orc!')
            board[player.location_i][player.location_j] = 0
        else:
            print('You hesitated, and were killed!')
            exit()

print_board(board, player)

while True:
    command = input('> ')
    #if command == 'print':
    #print_board(board, player)
    if command == 'quit' or command == 'exit':
        print('goodbye')
        break
    elif command == 'n':
        if player.location_j > 0:
            player.location_j -= 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 's':
        if player.location_j < height-1:
            player.location_j += 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'e':
        if player.location_i < width-1:
            player.location_i += 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    elif command == 'w':
        if player.location_i > 0:
            player.location_i -= 1
            check_location(board, player)
        else:
            print('you can\'t move there')
        print_board(board, player)
    else:
        print('I did not recognize that command')
