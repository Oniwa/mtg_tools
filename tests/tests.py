import unittest

from lib.deck import Deck
from lib.graveyard import Graveyard
from lib.hand import Hand
from lib.mtgsdk_wrapper import CardMock


class TestDelirium(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_deck_list(self):
        # John wants to calculate how often he will hit delirium off of a
        # turn 1 Vessel of Nascency in his GB Delirium deck.  To do this
        # he needs to load his deck list.
        gb_delirium = Deck()
        gb_delirium.load_text_list('D:\\code\\delirium\\tests\\test_data\\'
                                   'delirium.txt')

        # He knows the deck has sixty cards in it
        self.assertEqual(gb_delirium.size(), 60)

        # John then shuffles the deck
        gb_delirium.shuffle_deck()

        # John then draws 7 cards to his hand
        my_hand = Hand()

        my_hand.draw_starting_hand(gb_delirium)
        self.assertEqual(my_hand.size(), 7)

        # John realizes that he meant to get a a few specific cards in hand
        # first so he puts his hand back in the deck.

        count = 0
        while (my_hand.size() > 0) and (count < 400):
            my_hand.put_in_deck(my_hand.cards[0], gb_delirium)
            count += 1

        self.assertEqual(my_hand.size(), 0)

        # John gets a forest, swamp, and vessel in hand,
        # shuffles the deck, and then draws 4 more cards
        forest = CardMock(name='Forest', type='')
        swamp = CardMock(name='Swamp', type='')
        vessel = CardMock(name='Vessel of Nascency', type='')

        my_hand.get_card_from_deck(forest, gb_delirium)
        my_hand.get_card_from_deck(swamp, gb_delirium)
        my_hand.get_card_from_deck(vessel, gb_delirium)
        gb_delirium.shuffle_deck()
        my_hand.draw(4, gb_delirium)

        test_list = []
        for item in my_hand.cards:
            test_list.append(item.name)
        self.assertEqual(my_hand.size(), 7)
        self.assertIn(forest.name, test_list)
        self.assertIn(swamp.name, test_list)
        self.assertIn(vessel.name, test_list)

        # John plays the forest and the vessel on turn 1
        battlefield = []
        my_hand.play(forest, battlefield)
        my_hand.play(vessel, battlefield)

        self.assertEqual(my_hand.size(), 5)

        # On his next turn John draws a card, plays a swamp, and cracks the
        # Vessel choosing to put all cards in graveyard
        my_hand.draw(1, gb_delirium)
        my_hand.play(swamp, battlefield)

        self.assertEqual(my_hand.size(), 5)

        my_graveyard = Graveyard()

        for item in battlefield:
            if item.name == vessel.name:
                battlefield.remove(item)
                my_graveyard.cards.append(item)
                break

        gb_delirium.put_cards_in_graveyard(4, my_graveyard.cards)

        self.assertEqual(5, len(my_graveyard.cards))

        # check graveyard to see if delirium has been achieved
        my_graveyard.check_delirium()
        print(my_graveyard.delirium)
