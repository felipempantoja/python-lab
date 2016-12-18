from __future__ import print_function
import os
import random

class TicTacToe:
    def __init__(self):
        self.play_on = 'y'
        self.board = range(9)
        self.player = {1: 'x', 2: 'o'}
        self.current_player = random.randint(1,2)
        self.winning_sequences = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        self.messages = []

    def draw_board(self):
        print ('''
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
        ))

    def add_message(self, msg):
        self.messages += [msg]

    def print_messages(self):
        for i, msg in enumerate(self.messages):
            print(self.messages.pop(i))
    
    def toggle_player(self):
        self.current_player = 2 if self.current_player == 1 else 1
        return self.player[self.current_player]

    def get_remaining_positions(self):
        return map(str, [ e for e in self.board if type(e) is int ])

    def fill_board(self, position, player_assign):
        self.board[position] = player_assign

    def is_board_fullfilled(self):
        return all(type(e) is str for e in self.board)

    def is_current_player_winner(self):
        marker = self.player[self.current_player]
        for sequence in self.winning_sequences:
            board_seq = [ e for i, e in enumerate(self.board) if i in sequence ]
            if all(e == marker for e in board_seq):
                return True
        return False


game = TicTacToe()

while game.play_on == 'y':
    while True:
        os.system('clear')

        print('Welcome to Tic Tac Toe in Python')
        
        player = game.toggle_player()
        game.draw_board()
        game.print_messages()

        remaining_positions = game.get_remaining_positions()
        print('Remaining positions: {}'.format(', '.join(remaining_positions)))

        try:
            position = int(raw_input('Player {}: '.format(game.current_player)))
            if str(position) not in remaining_positions:
                game.add_message('Please, choose one of the remaining positions')
                continue
        except ValueError:
            game.add_message('Invalid number, try again')
            continue

        game.fill_board(position, player)

        if game.is_current_player_winner():
            game.add_message('Winner: Player {}'.format(game.current_player))
            break
        elif game.is_board_fullfilled():
            game.add_message('Draw!')
            break 

    os.system('clear')
    game.draw_board()
    game.print_messages()
    game.play_on = raw_input('End game. Play again (y/n): ')