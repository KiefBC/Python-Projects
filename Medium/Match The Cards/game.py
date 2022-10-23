# importing our cards
# randomize the import
import random

from cards import Card


class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ['Add', 'Boo', 'Cat', 'Dev',
                             'Egg', 'Far', 'Gum', 'Hut']
        self.columns = ['A', 'B', 'C', 'D']
        self.cards = []
        self.locations = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                location = f'{column}{num}'
                self.locations.append(location)

    def set_cards(self):
        # cant reuse locations right
        used_locations = []
        # loop thru card_options
        for word in self.card_options:
            # loop again to create 2 cards for every word
            # so we get full 16 cards
            for i in range(2):
                # set - set will remove duplicates
                available_locations = set(self.locations) - set(used_locations)
                random_location = random.choice(list(available_locations))
                used_locations.append(random_location)
                card = Card(word, random_location)
                self.cards.append(card)

    def create_row(self, num):
        row = []
        for column in self.columns:
            for card in self.cards:
                if card.location == f'{column}{num}':
                    if card.matched:
                        row.append(str(card))
                    else:
                        row.append('   ')

        return row

    def create_grid(self):
        # /    A    /    B    /     C
        header = '   |   ' + '   |   '.join(self.columns) + '   |'
        print(header)
        for row in range(1, self.size + 1):
            print_row = f'{row}| '
            get_row = self.create_row(row)
            print_row += ' | '.join(get_row) + '|'
            print(print_row)

    def check_match(self, loc1, loc2):
        cards = []
        for card in self.cards:
            if card.location == loc1 or card.location == loc2:
                cards.append(card)
        if cards[0] == cards[1]:
            cards[0].matched = True
            cards[1].matched = True
            return True
        else:
            for card in cards:
                print(f'{card.location}: {card}')
            return False

    def check_win(self):
        for card in self.cards:
            if card.matched == False:
                return False
        return True

    def check_location(self, time):
        while True:
            guess = input(f'whats the location of your {time} card?')
            if guess.upper() in self.locations:
                return guess.upper()
            else:
                print('thats not valid')

    def start_game(self):
        game_running = True
        print('Memory GAEM')
        self.set_cards()
        while game_running:
            self.create_grid()
            guess1 = self.check_location('first')
            guess2 = self.check_location('second')
            if self.check_match(guess1, guess2):
                if self.check_win():
                    print('congrats you win')
                    self.create_grid()
                    game_running = False
            else:
                input('those cards are not a match press enter to continue')
        print('GAME OVER')


if __name__ == '__main__':
    game = Game()
    game.start_game()
#    game.set_cards()
#    game.cards[0].matched = True
#    game.cards[1].matched = True
#    game.cards[2].matched = True
#    game.cards[3].matched = True
##    for card in game.cards:
#        print(card)
#    game.create_grid()
