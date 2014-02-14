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
        return randint(0, board_row_length)
    else:
        return randint(0, board_row_length - length)


def random_col(board, ship):
    length = ship['length']
    board_col_length = len(board[0])
    if ship['vertical']:
        return randint(0, board_col_length)
    else:
        return randint(0, board_col_length - length)


#propagates from an already defined origin
def generate_ship(ship):
    x = ship['origin'][0]
    y = ship['origin'][1]
    length = ship['length']
    prop = ship['propagate']
    if ship['vertical']:
        for position in range(0, length):
            inc_x = x + position * prop
            board[inc_x][y]['ship'] = ship['name']
    else:
        for position in range(0, length):
            inc_y = y + position * prop
            board[x][inc_y]['ship'] = ship['name']

#
# def in_sea(ship):
#     x = ship['origin'][0]
#     y = ship['origin'][1]
#     length = ship['length'] - 1
#     prop = ship['propagate']
#     if ship['vertical']:
#         if (x + length * prop < 0) or (x + length * prop > len(board) - 1):
#             return False
#         else:
#             return True
#     else:
#         if (y + length * prop < 0) or (y + length * prop > len(board[0]) - 1):
#             return False
#         else:
#             return True


def ship_collide(ship):
    x = ship['origin'][0]
    y = ship['origin'][1]
    length = ship['length']
    prop = ship['propagate']
    if ship['vertical']:
        for position in range(0, length):
            inc_x = x + position * prop
            if 'ship' in board[inc_x][y] and board[inc_x][y]['ship'] != ship['name']:
                return True
        else:
            return False
    else:
        for position in range(0, length):
            inc_y = y + position * prop
            if 'ship' in board[x][inc_y] and board[x][inc_y]['ship'] != ship['name']:
                return True
        else:
            return False


def board_position(ship):
    x = ship['origin'][0]
    y = ship['origin'][1]
    return board[x][y]


def is_real(ship):
    if in_sea(ship) is True:
        if ship_collide(ship) is True:
            return False
        else:
            return True
    else:
        return False


def seed_ship(ship):
    if ship in ships:
        ship['origin'] = [random_row(board), random_col(board)]
        ship['vertical'] = choice([True, False])
        ship['propagate'] = choice([-1, 1])


def place_ship(ship):
    seed_ship(ship)
    while is_real(ship) is False:
        seed_ship(ship)
    else:
        generate_ship(ship)


place_ship(battleship)
place_ship(destroyer)
place_ship(patrol)
print "battleship info: ", battleship
print "destroyer info: ", destroyer
print in_sea(destroyer), ship_collide(destroyer), is_real(destroyer)

for row in board:
    print row


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


