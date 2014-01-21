from random import randint
from random import choice
# This function adds individual dictionaries to a specified square board (edge by edge).  Cannot use the * function
# as with the original example because calling to one member of a list alters everything in that lists row.
def place_board(edge):
    board = []
    for i in range(0,edge):
        board.append([{'hit': False}])
        for j in range(0, edge-1):
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
          'propagate': -1,
          'hit': False}

destroyer = {'name': 'Destroyer',
             'origin': [],
             'length': 3,
             'vertical': False,
             'propagate': -1,
             'hit': False}

battleship = {'name': 'Battleship',
              'origin': [],
              'length': 4,
              'vertical': False,
              'propagate': -1,
              'hit': False}

ships = [patrol, destroyer, battleship]


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_loc = {}

#propagates from an already defined origin
def generate_ship(ship):
    x = ship['origin'][0]
    y = ship['origin'][1]
    length = ship['length']
    prop = ship['propagate']
    if ship['vertical']:
        for position in range(0, length):
            inc_x = x + position*prop
            board[inc_x][y]['ship'] = ship['name']
    else:
        for position in range(0, length):
            inc_y = y + position*prop
            board[x][inc_y]['ship'] = ship['name']

def in_sea(ship):
    x = ship['origin'][0]
    y = ship['origin'][1]
    length = ship['length'] - 1
    prop = ship['propagate']
    if ship['vertical']:
        if (x + length*prop < 0) or (x + length*prop > len(board) - 1):
            return False
        else:
            return True
    else:
        if (y + length*prop < 0) or (y + length*prop > len(board[0]) - 1):
            return False
        else:
            return True


def ship_collide(ship):
    x = ship['origin'][0]
    y = ship['origin'][1]
    length = ship['length'] - 1
    prop = ship['propagate']
    if ship['vertical']:
        for position in range(1, length):
            inc_x = x + position*prop
            if 'ship' in board[inc_x][y] and board[inc_x][y]['ship'] != ship['name']:
                return True
        else:
            return False
    else:
        for position in range(1, length):
            inc_y = y + position*prop
            if 'ship' in board[x][inc_y] and board[x][inc_y]['ship'] != ship['name']:
                return True
        else:
            return False


def board_position(ship):
    x = ship['origin'][0]
    y = ship['origin'][1]
    return board[x][y]


def place_ship(ship):
    if ship in ships:
        ship['origin'] = [random_row(board), random_col(board)]
        ship['vertical'] = choice([True, False])
        ship['propagate'] = choice([-1, 1])
        while not in_sea(ship) and ship_collide(ship):
            ship['origin'] = [random_row(board), random_col(board)]
        generate_ship(ship)




place_ship(destroyer)
place_ship(battleship)
print "destroyer info: ", destroyer
print "battleship info: ", battleship
for row in board:
    print row


#
# generate_ship(battleship)
# print "after generate_ship"
# for row in board:
#     print row
#
# if 'battleship'in board:
#     print board_position(battleship)
# # print board[destroyer['origin'][0]]
#

