board = range(0, 9)
player = {1: 'X', 2: 'O'}
current_player = 1
winner_sequences = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def draw_bord():
    print '''
    _{}_|_{}_|_{}_
    _{}_|_{}_|_{}_
     {} | {} | {}
    '''.format(board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8])

def print_remaining_positions():
    remaining_positions = map(str, [ e for e in board if type(e) is int ])
    print 'Remaining positions: {}'.format(', '.join(remaining_positions))

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
    print 'Results'


print 'Welcome to Tic Tac Toe in Python'

while not is_endgame(current_player):
    draw_bord()
    print_remaining_positions()
    position = int(raw_input('Player {}: '.format(current_player)))
    fill_board(position, player[current_player])
    current_player = 2 if current_player == 1 else 1
else:
    show_results()