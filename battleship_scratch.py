from random import randint
from random import choice
# This function adds individual dictionaries to a specified square board (edge by edge).  Cannot use the * function
# as with the original example because calling to one member of a list alters everything in that lists row.
def place_board(edge):
    board = []
    for i in range(0, edge):
        board.append([{'hit': False}])
        for j in range(0, edge - 1):
            board[i].append({'hit': False})
    return board


board = place_board(6)
#
# print 'Let's play Battleship!'
# print_board(board)

patrol = {'name': 'Patrol',
          'origin': [],
          'length': 2,
          'vertical': False,
          }

destroyer = {'name': 'Destroyer',
             'origin': [],
             'length': 3,
             'vertical': False,
             }

battleship = {'name': 'Battleship',
              'origin': [],
              'length': 4,
              'vertical': False,
              }

ships = [patrol, destroyer, battleship]


def random_row(board, ship):
    length = ship['length']
    board_row_length = len(board)
    if ship['vertical']:
        return randint(0, board_row_length - length)
    else:
        return randint(0, board_row_length - 1)


def random_col(board, ship):
    length = ship['length']
    board_col_length = len(board[0])
    if ship['vertical']:
        return randint(0, board_col_length - 1)
    else:
        return randint(0, board_col_length - length)


def seed_ship(ship):
    ship['vertical'] = choice([True, False])
    ship['origin'] = [random_row(board, ship), random_col(board, ship)]


def ship_collide(ship):
    origin_row = ship['origin'][0]
    origin_col = ship['origin'][1]
    length = ship['length']
    if ship['vertical']:
        for position in range(0, length):
            inc_row = origin_row + position
            if 'ship' in board[inc_row][origin_col] and board[inc_row][origin_col]['ship'] != ship['name']:
                return True
        else:
            return False
    else:
        for position in range(0, length):
            inc_col = origin_col + position
            if 'ship' in board[origin_row][inc_col] and board[origin_row][inc_col]['ship'] != ship['name']:
                return True
        else:
            return False


def generate_ship(ship):
    origin_row = ship['origin'][0]
    origin_col = ship['origin'][1]
    length = ship['length']
    if ship['vertical']:
        for position in range(0, length):
            inc_row = origin_row + position
            board[inc_row][origin_col]['ship'] = ship['name']
    else:
        for position in range(0, length):
            inc_col = origin_col + position
            board[origin_row][inc_col]['ship'] = ship['name']


def place_ship(ship):
    seed_ship(ship)
    while ship_collide(ship) is True:
        seed_ship(ship)
    else:
        generate_ship(ship)



place_ship(battleship)
place_ship(destroyer)
place_ship(patrol)
print "battleship info: ", battleship
print "destroyer info: ", destroyer
print ship_collide(destroyer)


def print_board(board):
    board_output = []
    for i in range(0, len(board)):
        board_output.append([" "])
        for j in range(0, len(board[0])):
            board_output[i].append(" ")
            if 'ship' in board[i][j]:
                # print i, j, board[i][j]['ship']
                board_output[i][j] = board[i][j]['ship'][0]
            elif board[i][j]['hit'] == False:
                board_output[i][j] = "X"
    for row in board_output:
        print " ".join(row)



print_board(board)
#

