import random


# DECK CLASS
class Deck():
    def __init__(self):
        self.build_deck()

    # make 5 decks of cards
    def build_deck(self):
        self.cards = []
        suits = ['♥', '♦', '♣', '♠']
        card_numbers = [' 2', ' 3', ' 4', ' 5', ' 6',
                        ' 7', ' 8', ' 9', '10', ' J', ' Q', ' K', ' A']
        card_value = 0
        for _ in range(5):
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

    def set_card_value(self, card, new_value):
        self.card = card
        self.new_value = new_value
        self.card.value = new_value


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
        self.bet = 0

    def deal_card(self):
        card = random.choice(deck.cards)

        # correct the value of aces in player's hand as needed
        if card[1] == 'A':
            self.num_of_aces += 1

        if self.num_of_aces > 1 and self.card_total + card[2] > 21:
            # TODO - set the value of an ace whose value is 11 to a value of 1, regardless of the ace's location in the deck
            # may use a function for this
            pass

        self.cards.append(card)
        self.card_total += card[2]
        deck.cards.remove(card)

    # show all cards face up
    def show_cards(self):
        player_cards = f'{self.name}\'s Total: {self.card_total} | '
        for suit, card_number, _ in self.cards:
            player_cards += (f'{card_number} {suit}  ')
        print(player_cards)

    # show one card face up, one face down - hide card total
    def show_dealer_cards(self):
        player_cards = f'{self.name}\'s Total: ?? | {self.cards[0][1]} {self.cards[0][0]}  ? ?'
        print(player_cards)


# PLAYER , DEALER, AND DECK CREATION
player = Player("Player", 1000)
dealer = Player("Dealer", 1000)
deck = Deck()

print('\nBLACKJACK - You vs The Dealer\nBankrupt the dealer to win!\n')


# GAME LOOP
while player.money > 0 and dealer.money > 0:

    if len(deck.cards) < 10:
        print('\nDeck has less than 10 cards left. Shuffling...\n')
        deck = Deck()

    print(f'{player.name} ${player.money} | {dealer.name} ${dealer.money} - Cards in Deck: {len(deck.cards)}')
    user_input = input('(B)et or (Q)uit? ')

    if user_input.lower() == 'b':
        player.clear_cards()
        dealer.clear_cards()
        player.bet = (abs(int(input('\nPlace your bets: $'))))
        player.deal_card()
        dealer.deal_card()
        player.deal_card()
        dealer.deal_card()

        print(f'\nDEAL!')
        player.show_cards()
        dealer.show_dealer_cards()

        # TODO - test this.
        # if player and dealer have natural 21...
        if ((player.cards[0][1] == 10 and player.cards[1][1] == ' A') or (player.cards[1][1] == 10 and player.cards[0][1] == ' A')) and ((dealer.cards[0][1] == 10 and dealer.cards[1][1] == ' A') or (dealer.cards[1][1] == 10 and dealer.cards[0][1] == ' A')):
            print('\nTie -  Natural 21\'s! You get back your bet money.\n')
            player.hit_me = False
            break
        # elif player has natural 21...
        elif (player.cards[0][1] == 10 and player.cards[1][1] == ' A') or (player.cards[1][1] == 10 and player.cards[0][1] == ' A'):
            print('\nNatural 21! You win 150 percent of your bet!\n')
            player.money += (player.bet * 1.5)
            dealer.money -= (player.bet * 1.5)
            break
        # else:
        # players asks 'hit_me'
        while player.hit_me:
            hit_input = input('\n(H)it or (S)tay? ')
            if hit_input.lower() == 'h':
                player.deal_card()
                player.show_cards()
                dealer.show_dealer_cards()

                if player.card_total > 21:
                    print('Sorry, you lose.\n')
                    player.money -= player.bet
                    dealer.money += player.bet
                    player.hit_me = False

            elif hit_input.lower() == 's':
                player.show_cards()
                dealer.show_cards()
                # TODO - look at the rest of the dealer rules, esp about dealer natural 21

                # if dealer total >= 17, dealer must stand
                # if dealer total <= 16, dealer must hit
                while dealer.card_total <= 16:
                    print('\nDealer Hits')
                    dealer.deal_card()
                    player.show_cards()
                    dealer.show_cards()

                if dealer.card_total <= 21 and dealer.card_total == player.card_total:
                    print('Standoff - you get back your bet money.')
                    player.hit_me = False

                elif dealer.card_total > 21 or player.card_total > dealer.card_total:
                    print('\nYou win!\n')
                    player.money += player.bet
                    dealer.money -= player.bet
                    player.hit_me = False
                else:
                    print('Sorry, you lose.\n')
                    player.money -= player.bet
                    dealer.money += player.bet
                    player.hit_me = False
                    break
            else:
                print('Invalid Input')

    elif user_input.lower() == 'q':
        break
    else:
        print('Invalid Input')


# GAME WRAP-UP
print(f'\nYou finish the game with ${player.money}')
if player.money >= 1000:
    print('You won money! Well Done!')
elif player.money <= 0:
    print('You have no money. You are an embarrassment to your ancestory! You try harder now!')
else:
    print('Nice try, you lost some money. Play again and do even better next time!')
