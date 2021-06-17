import random


class ValueNot2To500(Exception):
    pass


print('\nBLACKJACK - You vs The Dealer\n')


# DECK CLASS
class Deck():
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        suits = ['♥', '♦', '♣', '♠']
        card_numbers = [' 2', ' 3', ' 4', ' 5', ' 6',
                        ' 7', ' 8', ' 9', '10', ' J', ' Q', ' K', ' A']
        card_value = 0

        # build six decks of cards
        # card = [suit, card_number, card_value]
        for _ in range(6):
            for suit in suits:
                for card_number in card_numbers:
                    if card_number == ' J' or card_number == ' Q' or card_number == ' K':
                        card_value = 10
                    elif card_number == ' A':
                        card_value = 11
                    else:
                        card_value = int(card_number)
                    self.cards.append(
                        [suit, card_number, card_value])
        random.shuffle(self.cards)
        # print(f'Deck Count: {len(self.cards)}')


# PLAYER CLASS
class Player():
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.cards = []
        self.clear_cards()

    def clear_cards(self):
        self.cards.clear()
        self.card_total = 0
        self.hit_me = True
        self.num_of_aces = 0
        self.bet = int()

    def deal_card(self):
        card = deck.cards.pop()
       # see if the new card is an ace, and if the card_total is > 21. If so, change the ace to a value of 1.
        if self.card_total + card[2] > 21 and card[2] == 11:
            card[2] = 1

        self.cards.append(card)
        self.card_total += card[2]
        return card

    def show_cards(self):
        player_cards = f'{self.name}\'s Total: {self.card_total} | '
        for suit, card_number, _ in self.cards:
            player_cards += (f'{card_number} {suit}  ')
        print(player_cards)

    def dealer_show_cards(self):
        dealer_cards = f'{self.name}\'s Total: {self.cards[0][2]} | {self.cards[0][1]} {self.cards[0][0]}  ? ?'
        print(dealer_cards)

    def has_natural_21(self):
        if ((self.cards[0][2] == 10 and self.cards[1][2] == 11) or (self.cards[0][2] == 11 and self.cards[1][2] == 10)):
            return True
        return False


# PLAYER , DEALER, AND DECK CREATION
player = Player("Player", 1000)
dealer = Player("Dealer", 1000)
deck = Deck()


# GAME LOOP
while player.money > 0 and dealer.money > 0:
    print(f'{player.name} ${player.money} | {dealer.name} ${dealer.money}')
    user_input = input('(B)et or (Q)uit? ')

    if user_input.lower() == 'b':
        player.clear_cards()
        dealer.clear_cards()

        # Check that the bet is 2 <= bet <= 500, and is a number.
        while player.bet < 2 or player.bet > 500:
            try:
                player.bet = (
                    abs(int(input('\nPlace your bets ($2-$500): $'))))
                if player.bet < 2 or player.bet > 500:
                    raise ValueNot2To500
            except ValueNot2To500:
                print('\nError: Your bet is too low or too high.')
            except ValueError:
                print('\nInvalid input. Enter a number between 2 and 500.')

        # deal cards
        print(f'\nDEAL!')
        player.deal_card()
        dealer.deal_card()
        player.deal_card()
        dealer.deal_card()

        player.show_cards()
        dealer.dealer_show_cards()

        print(
            f'Natural 21s - Dealer: {dealer.has_natural_21()}  Player: {player.has_natural_21()}')

        # players asks 'hit_me'
        while player.hit_me:

            # if player and dealer have natural 21...
            if player.has_natural_21() and dealer.has_natural_21():
                player.show_cards()
                dealer.show_cards()
                print('\nTie -  Natural 21\'s! You get back your bet money.\n')
                # player.hit_me = False
                break
            # elif player has natural 21...
            elif player.has_natural_21() and not dealer.has_natural_21():
                print('\nNatural 21! You win 150 percent of your bet!\n')
                player.money += (player.bet * 1.5)
                dealer.money -= (player.bet * 1.5)
                player.show_cards()
                dealer.show_cards()
                # player.hit_me = False
                break
            elif not player.has_natural_21() and dealer.has_natural_21():
                print('\nDealer has Natural 21. Sorry, you lose.')
                player.money -= player.bet
                dealer.money += player.bet
                player.show_cards()
                dealer.show_cards()
                # player.hit_me = False
                break

            hit_input = input('\n(H)it or (S)tay? ')
            if hit_input.lower() == 'h':
                player.deal_card()
                player.show_cards()
                dealer.dealer_show_cards()

                if player.card_total > 21:
                    print('Sorry, you lose.\n')
                    player.money -= player.bet
                    dealer.money += player.bet
                    player.hit_me = False

            elif hit_input.lower() == 's':
                player.show_cards()
                dealer.show_cards()

                # if dealer total <= 16, dealer must hit
                while dealer.card_total < 17:
                    print('\nDealer hits...')
                    dealer.deal_card()
                    player.show_cards()
                    dealer.show_cards()

                if dealer.card_total > 21:
                    print('\nThe dealer busted out. YOU WIN!')
                    player.money += player.bet
                    dealer.money -= player.bet
                    player.hit_me = False

                elif player.card_total > dealer.card_total:
                    print('\nYOU WIN!')
                    player.money += player.bet
                    dealer.money -= player.bet
                    player.hit_me = False

                elif player.card_total == dealer.card_total:
                    player.show_cards()
                    dealer.show_cards()
                    print('\nTie! You get back your bet money.\n')

                else:
                    print('\nSorry, you lose.')
                    player.money -= player.bet
                    dealer.money += player.bet
                    player.hit_me = False
                    # break
            else:
                print('Invalid Input\n')

        # if there are 75 cards or less left in the deck, re-shuffle
        if len(deck.cards) < 75:
            deck = Deck()

    elif user_input.lower() == 'q':
        pass
    else:
        print('Invalid Input\n')


# GAME WRAP-UP
print(f'\nYou finish the game with ${player.money}')
if player.money >= 1000:
    print('Well Done!')
elif player.money <= 0:
    print('You are an embarrassment to your ancestory. You try harder now!')
else:
    print('Nice try! Play again and do even better next time!')
