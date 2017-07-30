import time

from graveyard import Graveyard
from hand import Hand

from lib.deck import Deck

start_time = time.time()

gb_delirium = Deck()
gb_delirium.load_text_list('D:\\code\\delirium\\tests\\test_data\\delirium.txt')
myhand = Hand()

count = 0
times_delirious = 0

while count < 100:
    gb_delirium.shuffle_deck()

    myhand.get_card_from_deck('Forest', gb_delirium)
    myhand.get_card_from_deck('Swamp', gb_delirium)
    myhand.get_card_from_deck('Vessel of Nascency', gb_delirium)
    gb_delirium.shuffle_deck()
    myhand.draw(4, gb_delirium)

    battlefield = []
    myhand.play('Forest', battlefield)
    myhand.play('Vessel of Nascency', battlefield)

    myhand.draw(1, gb_delirium)
    myhand.play('Swamp', battlefield)

    mygraveyard = Graveyard()
    battlefield.remove('Vessel of Nascency')
    mygraveyard.cards.append('Vessel of Nascency')
    gb_delirium.put_cards_in_graveyard(4, mygraveyard.cards)

    mygraveyard.check_delirium()
    if mygraveyard.delirium:
        times_delirious += 1

    for card in mygraveyard.cards:
        gb_delirium.put_in_deck(card)
    mygraveyard.cards = []

    for card in myhand.cards:
        gb_delirium.put_in_deck(card)
    myhand.cards = []

    gb_delirium.shuffle_deck()
    count += 1
    print(count)

percent = (times_delirious / count) * 100
print('There is a {}% chance to hit delirium with this deck on turn 2'
      ' with a vessel'.format(percent))
print("--- %s seconds ---" % (time.time() - start_time))