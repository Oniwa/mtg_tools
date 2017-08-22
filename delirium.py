"""
This script will determine the likely hood of getting delerium from a
vessel of nascency that is cracked on turn 2.  The assumption is that all
cards from the vessel will go into your graveyard and that you do not put a
card into your hand from vessel.  It also assumes that you start the game with
a forest, swamp, and vessel in you opening draw.
"""

import time

from lib.graveyard import Graveyard
from lib.hand import Hand
from lib.mtgsdk_wrapper import CardMock
from lib.deck import Deck

# Start timer for profiling purposes
start_time = time.time()

# import the deck list
gb_delirium = Deck()
gb_delirium.load_text_list('D:\\code\\delirium\\tests\\test_data\\delirium.txt')

# Initialize hand, battlefield, and graveyard
my_hand = Hand()
my_graveyard = Graveyard()
battlefield = []

# Mock cards to be used in model
forest = CardMock(name='Forest')
swamp = CardMock(name='Swamp')
vessel = CardMock(name='Vessel of Nascency')

# Variables
deck_size = len(gb_delirium.cards)  # Initial size of imported deck
count = 0  # Number of times model ran
times_delirious = 0  # Number of times model found delirium was achieved

# Run model 10000 times
while count < 10000:
    gb_delirium.shuffle_deck()

    # Get swamp, forest, and vessel in hand then draw 4 more cards
    my_hand.get_card_from_deck(forest, gb_delirium)
    my_hand.get_card_from_deck(swamp, gb_delirium)
    my_hand.get_card_from_deck(vessel, gb_delirium)
    gb_delirium.shuffle_deck()
    my_hand.draw(4, gb_delirium)

    # Turn 1
    my_hand.play(forest, battlefield)
    my_hand.play(vessel, battlefield)

    # Turn 2
    #  Assumption: You do not return a card from vessel
    my_hand.draw(1, gb_delirium)
    my_hand.play(swamp, battlefield)

    for item in battlefield:
        if item.name == vessel.name:
            battlefield.remove(item)
            my_graveyard.cards.append(item)
            break

    gb_delirium.put_cards_in_graveyard(4, my_graveyard.cards)

    my_graveyard.check_delirium()
    if my_graveyard.delirium:
        times_delirious += 1

    # Reset hand, deck, graveyard, and battlefield to original condition
    # so that we can rerun the model
    for card in my_graveyard.cards:
        gb_delirium.put_in_deck(card)
    my_graveyard.cards = []
    my_graveyard.delirium = False

    for card in my_hand.cards:
        gb_delirium.put_in_deck(card)
    my_hand.cards = []

    for card in battlefield:
            gb_delirium.put_in_deck(card)
    battlefield = []

    gb_delirium.shuffle_deck()
    count += 1

    # Check to see if deck was properly reset
    if len(gb_delirium.cards) != deck_size:
        print('Error resetting play state')
        break

# Run statistics on model and report
percent = (times_delirious / count) * 100
print('There is a {}% chance to hit delirium with this deck on turn 2'
      ' with a vessel'.format(percent))
print("--- %s seconds ---" % (time.time() - start_time))
