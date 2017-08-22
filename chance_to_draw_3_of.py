"""
This script will determine the likely hood that you draw a specific card that
you only have three copies of by a specific turn.  Assumption is that you draw
first.
"""

from lib.hand import Hand
from lib.mtgsdk_wrapper import CardMock
from lib.deck import Deck

surgical = CardMock(name='Surgical Extraction')

my_deck = Deck()
my_deck.load_text_list('D:\\code\\delirium\\tests\\test_data\\draw_3_of.txt')

turn = 3  # Change this variable to change the turn number to find the card by

my_hand = Hand()
deck_size = len(my_deck.cards)
count = 0
draw_3_of = 0

while count < 10000:
    my_deck.shuffle_deck()

    my_hand.draw_starting_hand(my_deck)
    my_hand.draw(turn, my_deck)

    for card in my_hand.cards:
        if card.name == surgical.name:
            draw_3_of += 1
            break

    for card in my_hand.cards:
        my_deck.put_in_deck(card)
    my_hand.cards = []

    if len(my_deck.cards) != deck_size:
        print('Error resetting game state')
        break

    count += 1

percent = draw_3_of / count * 100
print("There is a {}% chance that you will draw the "
      "specific card by turn ()".format(percent, turn))

