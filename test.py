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

class Game:
    def __init__(self):
        self.dealer_one = Card()
        self.dealer_two = Card()
        self.dealer_hand = []
        self.dealer_hand.append(self.dealer_one)
        self.dealer_hand.append(self.dealer_two)

        self.player_one = Card()
        self.player_two = Card()
        self.player_hand = []
        self.player_hand.append(self.player_one)
        self.player_hand.append(self.player_two)

    def get_hand_value(self, hand):
        total = 0
        
        for card in hand:
            total += card.get_value()
        return total

    def run_game(self):
        gamestate = True

        while gamestate:
            print('You\'ve been dealt a ' + self.player_one.print_card() + '!')
            print('You\'ve been dealt a ' + self.player_two.print_card() + '!')
            print('Would you like to: 1. Hit 2. Stay')
            response = input()
            if response == '1':
                self.player_hand.append(Card())
                print('You got a ' + self.player_hand[-1].print_card())
                if self.get_hand_value(self.player_hand) > 21:
                    gamestate = False
                    print('you fucking suck, you lost all your money')
            elif response == '2':
                if self.get_hand_value(self.player_hand) > self.get_hand_value(self.dealer_hand) and self.get_hand_value(self.player_hand) <= 21:
                    print('You win you fat fucker')
                else:
                    print('You Lose')
                gamestate = False




newgame = Game()
newgame.run_game()




