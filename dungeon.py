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

player = Player('Link', 0, 0)

while True:
   command = input('> ')
   if command == 'print':
       print_board(board, player)
   elif command == 'quit' or command == 'exit':
       print('goodbye')
       break
   elif command == 'north':
       if player.location_j > 0:
           player.location_j -= 1
       else:
           print('you can\'t move there')
       print_board(board, player)
   elif command == 'south':
       if player.location_j < height-1:
           player.location_j += 1
       else:
           print('you can\'t move there')
       print_board(board, player)
   elif command == 'east':
       if player.location_i < width-1:
           player.location_i += 1
       else:
           print('you can\'t move there')
       print_board(board, player)
   elif command == 'west':
       if player.location_i > 0:
           player.location_i -= 1
       else:
           print('you can\'t move there')
       print_board(board, player)
   else:
       print('I did not recognize that command')
