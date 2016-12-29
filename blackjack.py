class Player(object):
    
    amount_money = 2500

    def __init__(self):
        self.name = raw_input('Player name: ')

    def play_on(self):
        play_on = raw_input('Play on (y/n): ')
        return True if play_on == 'y' else False

    def has_money(self):
        return Player.amount_money > 0

class Game(object):

    def __init__(self):
        self.player = Player()

    def play_on(self):
        return self.player.play_on() and self.player.has_money()

    def start(self):
        bet = raw_input('How much you want to bet? (Available: {}): '.format(self.player.amount_money))
        print bet
        

game = Game()

while True:
    game.start()
    if not game.play_on():
        break

print 'Thanks!'