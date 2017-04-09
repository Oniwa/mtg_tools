import unittest

from deck import Deck
from hand import Hand

class TestDelirium(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_decklist(self):
        # John wants to calculate how often he will hit delirium off of a
        # turn 1 Vessel of Nascency in his GB Delirium deck.  To do this
        # he needs to load his decklist.
        gb_delirium = Deck()
        gb_delirium.load_text_list('D:\\code\\delirium\\tests\\test_data\\delirium.txt')

        # He knows the deck has sixty cards in it
        self.assertEqual(gb_delirium.size(), 60)

        # John then shuffles the deck
        gb_delirium.shuffle_deck()

        # John then draws 7 cards to his hand
        myhand = Hand()

        myhand.draw_starting_hand(gb_delirium)
        self.assertEqual(myhand.size(), 7)

        # John realizes that he meant to get a a few specific cards in hand
        # first so he puts his hand back in the deck.

        count = 0
        while (myhand.size() > 0) and (count < 400):
            myhand.put_in_deck(myhand.cards[0], gb_delirium)
            count += 1

        self.assertEqual(myhand.size(), 0)

        # John gets a forest, swamp, and vessel in hand then draws 4 more cards
        myhand.get_card_from_deck('Forest', gb_delirium)
        myhand.get_card_from_deck('Swamp', gb_delirium)
        myhand.get_card_from_deck('Vessel of Nascency', gb_delirium)
        myhand.draw(4, gb_delirium)

        self.assertEqual(myhand.size(), 7)
        self.assertIn('Forest', myhand.cards)
        self.assertIn('Swamp', myhand.cards)
        self.assertIn('Vessel of Nascency', myhand.cards)

        # John plays the forest and the vessel on turn 1
        battlefield = []