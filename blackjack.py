#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from random import randint
import os
import platform

class Someone(object):
    def __init__(self):
        self.current_cards = []

    def hit(self, pack):
        self.current_cards.append(pack.pop_card())

    def show_hands(self, end_game=False):
        cards = self.current_cards[:] #making a copy of the original list
        total_cards = len(cards)
        hands_points = self.hands_points()

        if type(self) == Dealer: current = 'DEALER'
        else: current = 'PLAYER'
        
        if type(self) == Dealer and not end_game:
            hands_points = '? + {}'.format(cards[1].points)
            cards[0] = Card('?', '?', 0) 

        print '\n==== {} HANDS ===='.format(current)

        print ( '┌─────────┐' ) * total_cards
        print ( '|{}       |'  * total_cards ).format( *[c.value.ljust(2, ' ') for c in cards] )
        print ( '|         |' ) * total_cards
        print ( '|         |' ) * total_cards
        print ( '|    {}    |'  * total_cards ).format( *[c.symbol for c in cards] )
        print ( '|         |' ) * total_cards
        print ( '|         |' ) * total_cards
        print ( '│       {}│'   * total_cards ).format( *[c.value.rjust(2, ' ') for c in cards] )
        print ( '└─────────┘' ) * total_cards
        
        print 'Total points: {}'.format(hands_points)

    def hands_points(self):
        card_points = map(lambda x: x.points, self.current_cards)

        lst_non_aces_points = filter(lambda x: type(x) is not tuple, card_points)
        lst_aces_points = filter(lambda x: type(x) is tuple, card_points)

        sum_non_aces_points = sum(lst_non_aces_points)
        sum_aces_points = len(lst_aces_points) * 11 # sum([ a[-1] for a in lst_aces_points ])

        sum_all = sum_aces_points + sum_non_aces_points
        
        used_max_aces_points = len(lst_aces_points)

        while sum_all > Game.MAX_POINTS and used_max_aces_points > 0:
            sum_all -= 10
            used_max_aces_points -= 1

        return sum_all
    

class Dealer(Someone):
    def play(self, pack, player):
        while self.hands_points() < Game.MAX_POINTS and self.hands_points() < player.hands_points() and pack.has_cards():
            self.hit(pack)

class Player(Someone):
    amount_money = 2500

    def __init__(self):
        super(Player, self).__init__()
        self.name = raw_input('Player name: ')
        self.current_bet = None

    def play_on(self):
        play_on = raw_input('\nPlay on (y/n): ')
        return True if play_on == 'y' else False

    def has_money(self):
        return self.amount_money > 0

    def make_a_bet(self):
        while True:
            try:
                bet = int(raw_input('How much you want to bet? (Available: {}): '.format(self.amount_money)))
                if bet > self.amount_money:
                    print 'You dont have this amount, please choose an amount less than {}'.format(self.amount_money)
                else:
                    self.current_bet = bet
                    self.amount_money -= bet
                    break
            except ValueError:
                print 'Please type a numeric input'

    def stand(self):
        pass


class Card(object):
    def __init__(self, symbol, value, points):
        self.symbol = symbol
        self.value = value
        self.points = points


class CardPack(object):
    def __init__(self):
        self.cards = []
        for symbol in ['♠', '♦', '♥', '♣']:
            self.cards += [ Card(symbol, 'A', (1, 11)) ]
            self.cards += [ Card(symbol, str(points), points) for points in range(2, 11) ]
            self.cards += [ Card(symbol, value, 10) for value in ['J', 'Q', 'K'] ]

    def distribute(self):
        return [self.pop_card(), self.pop_card()]
    
    def pop_card(self):
        return self.cards.pop(randint(0, len(self.cards) - 1))

    def has_cards(self):
        return len(self.cards) > 0


class Game(object):
    MAX_POINTS = 21

    @staticmethod
    def clear_output():
        if platform.system() == 'Windows': os.system('cls')
        else: os.system('clear')

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.winner = None

    def draw_ui(self):
        choice = -1
        while True:
            Game.clear_output()
            
            self.player.show_hands()
            self.dealer.show_hands()

            print '\nThat is your turn, {}. '.format(self.player.name)
            print '(1) Hit'
            print '(2) Stand'
            print '(3) Double Down'
            print '(4) Split'
            print '(5) Surrender'
            try:
                choice = int(raw_input('\nWhat do you want to do now? '))

                if choice not in (1,2,3,4,5):
                    continue

                if choice == 1: 
                    self.player.hit(self.pack)
                    keep_playing = self.calculate()
                    if not keep_playing:
                        break
                elif choice == 2: 
                    self.dealer.play(self.pack, self.player)
                    if self.player.hands_points() > self.dealer.hands_points() or self.dealer.hands_points() > Game.MAX_POINTS:
                        self.set_winner(self.player)
                        self.pay_player()
                    elif self.dealer.hands_points() == self.player.hands_points():
                        self.set_winner(None)
                    else:
                        self.set_winner(self.dealer)
                    break
                
            except ValueError as e:
                print e
                pass
    
    def calculate(self):
        if self.player.hands_points() > Game.MAX_POINTS:
            self.set_winner(self.dealer)
            return False
        elif self.player.hands_points() == Game.MAX_POINTS:
            self.dealer.play(self.pack, self.player)
            if self.dealer.hands_points() == Game.MAX_POINTS:
                self.set_winner(None)
            else:
                self.set_winner(self.player)
                self.pay_player()

            return False
        return True

    def set_winner(self, winner):
        self.winner = winner

    def show_winner(self):
        if self.winner == None:
            print 'Draw!'
        elif type(self.winner) == Player:
            print 'Congratulations, {}, you win!'.format(self.player.name)
        else:
            print 'You lose.' 

    def pay_player(self):
        self.player.amount_money += self.player.current_bet * 2

    def start(self):
        Game.clear_output()

        self.pack = CardPack()
        self.player.make_a_bet()

        self.player.current_cards = self.pack.distribute()
        self.dealer.current_cards = self.pack.distribute()
        
        self.draw_ui()      

game = Game()

while True:
    game.start()

    Game.clear_output()

    game.player.show_hands()
    game.dealer.show_hands(end_game=True)

    game.show_winner()

    if not game.player.play_on():
        print 'Thanks for playing!'
        break
    if not game.player.has_money():
        print 'You dont have money :/'
        break