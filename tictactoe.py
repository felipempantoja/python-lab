from subprocess import call

board = range(9)
player = {1: 'X', 2: 'O'}
current_player = 2
winner_sequences = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def draw_board():
    print '''
    _{}_|_{}_|_{}_
    _{}_|_{}_|_{}_
     {} | {} | {}
    '''.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])

def get_remaining_positions():
    return map(str, [ e for e in board if type(e) is int ])

def fill_board(position, player_assign):
    board[position] = player_assign

def is_endgame(current_player):
    return is_board_fullfilled() or is_winner(current_player)

def is_board_fullfilled():
    return all(type(e) is str for e in board)

def is_winner(current_player):
    signal = player[current_player]
    for sequence in winner_sequences:
        board_seq = [ e for i, e in enumerate(board) if i in sequence ]
        if all(e == signal for e in board_seq):
            return True
    return False
    
def show_results():
    print '\n\nResults'
    if is_winner(current_player):
        print 'Winner: Player {}'.format(current_player)
    elif is_board_fullfilled():
        print 'Draw!'


print 'Welcome to Tic Tac Toe in Python'

while not is_endgame(current_player):
    current_player = 2 if current_player == 1 else 1
    # call(['clear'])
    draw_board()
    remaining_positions = get_remaining_positions()
    print 'Remaining positions: {}'.format(', '.join(remaining_positions))
    try:
        position = int(raw_input('Player {}: '.format(current_player)))
        if str(position) not in remaining_positions:
            print 'Please, choose one of the remaining positions'
            continue
    except ValueError:
        print 'Invalid number, try again'
        continue
    fill_board(position, player[current_player])
else:
    show_results()