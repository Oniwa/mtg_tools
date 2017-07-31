import time

from lib.graveyard import Graveyard
from lib.hand import Hand
from mtgsdk import Card
from lib.mtgsdk_wrapper import get_card
from lib.deck import Deck

start_time = time.time()

gb_delirium = Deck()
gb_delirium.load_text_list('D:\\code\\delirium\\tests\\test_data\\delirium.txt')
myhand = Hand()
mygraveyard = Graveyard()

deck_size = len(gb_delirium.cards)

forest = Card()
forest.name = 'Forest'

swamp = Card()
swamp.name = 'Swamp'

vessel = Card()
vessel.name = 'Vessel of Nascency'


count = 0
times_delirious = 0

while count < 10000:
    gb_delirium.shuffle_deck()

    myhand.get_card_from_deck(forest, gb_delirium)
    myhand.get_card_from_deck(swamp, gb_delirium)
    myhand.get_card_from_deck(vessel, gb_delirium)
    gb_delirium.shuffle_deck()
    myhand.draw(4, gb_delirium)

    battlefield = []
    myhand.play(forest, battlefield)
    myhand.play(vessel, battlefield)

    myhand.draw(1, gb_delirium)
    myhand.play(swamp, battlefield)

    for item in battlefield:
        if item.name == vessel.name:
            battlefield.remove(item)
            mygraveyard.cards.append(item)
            break

    gb_delirium.put_cards_in_graveyard(4, mygraveyard.cards)

    mygraveyard.check_delirium()
    if mygraveyard.delirium:
        times_delirious += 1

    for card in mygraveyard.cards:
        gb_delirium.put_in_deck(card)
    mygraveyard.cards = []
    mygraveyard.delirium = False

    for card in myhand.cards:
        gb_delirium.put_in_deck(card)
    myhand.cards = []

    for card in battlefield:
            gb_delirium.put_in_deck(card)
    battlefield = []

    gb_delirium.shuffle_deck()
    count += 1

    if len(gb_delirium.cards) != deck_size:
        print('Error resetting play state')
        break

percent = (times_delirious / count) * 100
print('There is a {}% chance to hit delirium with this deck on turn 2'
      ' with a vessel'.format(percent))
print("--- %s seconds ---" % (time.time() - start_time))
