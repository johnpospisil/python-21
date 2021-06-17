
import random

print('\nBLACKJACK - You vs The Dealer\n')

# PLAYER CLASS


class Player():
    def __init__(self, money):
        self.money = money
        self.hit_me = True
        self.cards = []
        self.bet = 0
        self.card_total = 0


# FUNCTIONS
def build_deck():
    suits = ['Hearts  ', 'Diamonds', 'Clubs   ', 'Spades  ']
    card_numbers = [' 2', ' 3', ' 4', ' 5', ' 6',
                    ' 7', ' 8', ' 9', '10', ' J', ' Q', ' K', ' A']
    deck = []  # a list of lists [[suit, card_number, value], ...]
    card_value = 0
    for suit in suits:
        for card_number in card_numbers:
            if card_number == ' J' or card_number == ' Q' or card_number == ' K':
                card_value = 10
            elif card_number == ' A':
                card_value = 11
            else:
                card_value = int(card_number)
            deck.append([suit, card_number, card_value])
    return deck


def deal_card():
    card = random.choice(deck)
    temp_card = card
    deck.remove(card)
    return temp_card


def show_cards():
    player_cards = f'Player: '
    dealer_cards = f'Dealer: '
    for suit, card_number, _ in player.cards:
        player_cards += (f'{card_number} {suit}  ')
    for suit, card_number, _ in dealer.cards:
        dealer_cards += (f'{card_number} {suit}  ')

    print(player_cards)
    print(dealer_cards)


# calculate player and dealer scores
def get_card_total(plr):
    for _, _, value in plr.cards:
        plr.card_total += value
        return plr.card_total


def clear_cards():
    player.cards.clear()
    dealer.cards.clear()


# PLAYER , DEALER, AND DECK CREATION
player = Player(10000)
dealer = Player(1000)
deck = build_deck()

# GAME LOOP
while player.money > 0 and dealer.money > 0:
    print(f'Player ${player.money} | Dealer ${dealer.money}')
    user_input = input('(P)lay or (Q)uit? ')

    if user_input.lower() == 'p':
        clear_cards()
        player.bet = abs(int(input('\nPlace your bets: $')))
        player.cards.append(deal_card())
        player.cards.append(deal_card())
        dealer.cards.append(deal_card())
        dealer.cards.append(deal_card())
        print(f'\nDEAL!')
        show_cards()

        # if player and dealer have natural 21...
        if (player.cards[0][1] == 10 and player.cards[1][1] == ' A' or player.cards[1][1] == 10 and player.cards[0][1] == ' A') and (dealer.cards[0][1] == 10 and dealer.cards[1][1] == ' A' or dealer.cards[1][1] == 10 and dealer.cards[0][1] == ' A'):
            print('Tie Natural 21\'s! You get back your bet money.\n')
            break
        # elif player has natural 21...
        elif player.cards[0][1] == 10 and player.cards[1][1] == ' A' or player.cards[1][1] == 10 and player.cards[0][1] == ' A':
            print('Natural 21! You win 150 percent of your bet!\n')
            player.money += (player.bet * 1.5)
            dealer.money -= (player.bet * 1.5)
            break

        # players asks 'hit_me'
        while player.hit_me:
            hit_input = input('\n(H)it or (S)tay?')
            if hit_input.lower() == 'h':
                player.cards.append(deal_card())
                show_cards()

                print(f'\nCard Total is: {get_card_total(player)}\n')

                # change Ace from 11 to 1 point if needed
                if player.cards[-1][1] == ' A' and player.card_total > 21:
                    player.cards[-1][1] = 1

            elif hit_input.lower() == 's':
                # TODO - dealer looks at total and decides if he hits or not
                player.hit_me = False
                break
            else:
                print('Invalie Input')
        # player.cards
        # TODO - sum the player.card values, same for the dealer.
        if get_card_total(player) > get_card_total(dealer):
            print('You win!\n')
            player.money += player.bet
            dealer.money -= player.bet
        else:
            print('Sorry, you lose.\n')
            player.money -= player.bet
            dealer.money += player.bet
    elif user_input.lower() == 'q':
        break
    else:
        print('Invalid Input')

# GAME WRAP-UP
print(f'\nYou finish the game with ${player.money}')
if player.money >= 10000:
    print('Well Done!')
elif player.money <= 0:
    print('You are an embarrassment to your ancestory. You try harder now!')
else:
    print('Nice try! Play again and do even better next time!')
