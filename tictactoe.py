class TicTacToe:
    def __init__(self):
        self.board = range(9)
        self.player = {1: 'x', 2: 'o'}
        self.current_player = 2
        self.winning_sequences = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def draw_board(self):
        print '''
        _{}_|_{}_|_{}_
        _{}_|_{}_|_{}_
         {} | {} | {}
        '''.format(
            self.board[0],
            self.board[1],
            self.board[2],
            self.board[3],
            self.board[4],
            self.board[5],
            self.board[6],
            self.board[7],
            self.board[8]
        )
    
    def toggle_player(self):
        self.current_player = 2 if self.current_player == 1 else 1
        return self.player[self.current_player]

    def get_remaining_positions(self):
        return map(str, [ e for e in self.board if type(e) is int ])

    def fill_board(self, position, player_assign):
        self.board[position] = player_assign

    def is_running(self):
        return not game.is_board_fullfilled() and not game.is_current_player_winner()

    def is_board_fullfilled(self):
        return all(type(e) is str for e in self.board)

    def is_current_player_winner(self):
        signal = self.player[self.current_player]
        for sequence in self.winning_sequences:
            board_seq = [ e for i, e in enumerate(self.board) if i in sequence ]
            if all(e == signal for e in board_seq):
                return True
        return False
        
    def show_results(self):
        print '\n\nResults'
        if self.is_current_player_winner():
            print 'Winner: Player {}'.format(self.current_player)
        elif self.is_board_fullfilled():
            print 'Draw!' 


print 'Welcome to Tic Tac Toe in Python'

game = TicTacToe()

while game.is_running():
    player = game.toggle_player()
    game.draw_board()

    remaining_positions = game.get_remaining_positions()
    print 'Remaining positions: {}'.format(', '.join(remaining_positions))

    try:
        position = int(raw_input('Player {}: '.format(game.current_player)))
        if str(position) not in remaining_positions:
            print 'Please, choose one of the remaining positions'
            continue
    except ValueError:
        print 'Invalid number, try again'
        continue

    game.fill_board(position, player)
else:
    game.show_results()