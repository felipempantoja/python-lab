#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from random import randint
import os

class Dealer(object):
    def __init__(self):
        self.current_cards = []

    def show_hands(self, end_game=False):
        if end_game:
            print 'Dealer hands: {} = {}'.format(self.current_cards, self.hands_length())
        else:
            print 'Dealer hands: {}, ? = ?'.format(self.current_cards[0])

    def hands_length(self):
        return reduce(lambda a,b: a+b, map(lambda x: x.length, self.current_cards))

        '''length = reduce(lambda a,b: a+b, map(lambda x: x.length, self.current_cards))
        while length > Game.max_length:
            for card in self.current_cards:
                if card.alternative_length and card.alternative_length != card.length:
                    length -= card.alternative_length + card.length
                    card.replace_length()
                    continue
            break'''

    def play(self, pack, player):
        while self.hands_length() < Game.max_length and self.hands_length() < player.hands_length() and pack.has_cards():
            self.hit(pack)

    def hit(self, pack):
        self.current_cards.append(pack.pop_card())


class Player(object):
    amount_money = 2500

    def __init__(self):
        self.name = raw_input('Player name: ')
        self.current_cards = []
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

    def hit(self, pack):
        self.current_cards.append(pack.pop_card())

    def stand(self):
        pass

    def show_hands(self):
        print '\nPlayer hands: {} = {}'.format(self.current_cards, self.hands_length())

    def hands_length(self):
        return reduce(lambda a,b: a+b, map(lambda x: x.length, self.current_cards))


class Card(object):
    def __init__(self, name, length, alternative_length=None):
        self.name = name
        self.length = length
        self.alternative_length = alternative_length

    def replace_length(self):
        if self.alternative_length:
            self.length = self.alternative_length

    def __repr__(self):
        return '{} - {}'.format(self.name, self.length)


class CardPack(object):
    def __init__(self):
        self.cards = [
            Card('🂡', 11, 1),
            Card('🂢', 2),
            Card('🂣', 3),
            Card('🂤', 4),
            Card('🂥', 5),
            Card('🂦', 6),
            Card('🂧', 7),
            Card('🂨', 8),
            Card('🂩', 9),
            Card('🂪', 10),
            Card('🂫', 10),
            Card('🂭', 10),
            Card('🂮', 10)
        ]

    def distribute(self):
        return [self.pop_card(), self.pop_card()]
    
    def pop_card(self):
        return self.cards.pop(randint(0, len(self.cards) - 1))

    def has_cards(self):
        return len(self.cards) > 0


class Game(object):
    max_length = 21

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()

    def play_on(self):
        return self.player.play_on() and self.player.has_money()

    def open_menu(self):
        choice = -1
        while True:
            print '\nThat is your turn, {}. '.format(self.player.name)
            print '(1) Hit'
            print '(2) Stand'
            print '(3) Double Down'
            print '(4) Split'
            print '(5) Surrender'
            try:
                choice = int(raw_input('\nWhat do you want to do now? '))

                # os.system('clear')
                print choice

                if choice not in (1,2,3,4,5):
                    continue

                if choice == 1: 
                    self.player.hit(self.pack)
                    self.player.show_hands()
                    self.dealer.show_hands()
                    
                    keep_playing = self.calculate()
                    if not keep_playing:
                        break
                elif choice == 2: 
                    self.dealer.play(self.pack, self.player)
                    if self.player.hands_length() > self.dealer.hands_length() or self.dealer.hands_length() > Game.max_length:
                        print 'You win!'
                        self.pay_player()
                    elif self.dealer.hands_length() == self.player.hands_length():
                        print 'Draw!'
                    else:
                        print 'Busting!'
                        print 'You lose.'
                    break
                
            except ValueError as e:
                print e
                pass
    
    def calculate(self):
        if self.player.hands_length() > Game.max_length:
            print 'Busting!'
            print 'You lose.'
            return False
        elif self.player.hands_length() == Game.max_length:
            self.dealer.play(self.pack, self.player)
            if self.dealer.hands_length() == Game.max_length:
                print 'Draw!'
            else:
                print 'You win!'
                self.pay_player()

            return False
        return True

    def pay_player(self):
        self.player.amount_money += self.player.current_bet * 2

    def start(self):
        self.pack = CardPack()
        self.player.make_a_bet()

        self.player.current_cards = self.pack.distribute()
        self.dealer.current_cards = self.pack.distribute()
        
        self.player.show_hands()
        self.dealer.show_hands()
        
        self.open_menu()      

game = Game()

while True:
    game.start()

    game.player.show_hands()
    game.dealer.show_hands(end_game=True)

    if not game.player.play_on():
        print 'Thanks for playing!'
        break
    if not game.player.has_money():
        print 'You dont have money :/'
        break