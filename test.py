import random

class Card:
    def __init__(self):
        self.card_num = random.randint(1,13) 
        self.card_dict = {} 
        self.card_dict[1] = 'Ace' 
        self.card_dict[2] = 'Two' 
        self.card_dict[3] = 'Three' 
        self.card_dict[4] = 'Four' 
        self.card_dict[5] = 'Five' 
        self.card_dict[6] = 'Six' 
        self.card_dict[7] = 'Seven' 
        self.card_dict[8] = 'Eight' 
        self.card_dict[9] = 'Nine' 
        self.card_dict[10] = 'Ten' 
        self.card_dict[11] = 'Jack' 
        self.card_dict[12] = 'Queen' 
        self.card_dict[13] = 'King'

    def get_value(self):
        if self.card_num >= 10:
            return 10
        else:
            return self.card_num
    def print_card(self):
        return self.card_dict[self.card_num]

class Player:
    def __init__(self):
        self.hand = [Card(), Card()]
    
    def hit(self):
        self.hand.append(Card())

    def get_hand_value(self):
        total = 0
        
        for card in self.hand:
            total += card.get_value()
        return total

class Game:
    def __init__(self):
        self.Dealer = Player()
        self.Human = Player()



    def run_game(self):
        gamestate = True

        while gamestate:
            print('You\'ve been dealt a ' + self.Human.hand[0].print_card() + '!')
            print('You\'ve been dealt a ' + self.Human.hand[1].print_card() + '!')
            print('Would you like to: 1. Hit 2. Stay')
            response = input()
            if response == '1':
                self.Human.hit()
                print('\nYou got a ' + self.Human.hand[-1].print_card()) # check last card in hand
                if self.Human.get_hand_value() > 21:
                    gamestate = False
                    print('you fucking suck, you lost all your money')
                else: # Assuming you didn't lose ;)
                    if self.Dealer.get_hand_value() <=17: # Dealer must hit if under 17 
                        self.Dealer.hit()

            elif response == '2':

                if self.Dealer.get_hand_value() <=17: # Dealer must hit if under 17 
                    self.Dealer.hit()

                if self.Human.get_hand_value() > self.Dealer.get_hand_value() and self.Human.get_hand_value() <= 21 or self.Dealer.get_hand_value() > 21:
                    print('Your hand: ' + str(self.Human.get_hand_value()))
                    print('Dealer hand: ' + str(self.Dealer.get_hand_value()))
                    print('You win you fat fucker')
                else:
                    print('Your hand: ' + str(self.Human.get_hand_value()))
                    print('Dealer hand: ' + str(self.Dealer.get_hand_value()))
                    print('You Lose')
                gamestate = False




newgame = Game()
newgame.run_game()




