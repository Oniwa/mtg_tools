import unittest

from deck import Deck
from hand import Hand

class TestHand(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_draw_starting_hand(self):
        deck_location = 'D:\\code\\delirium\\tests\\test_data\\delirium.txt'

        gb_delirium = Deck()

        gb_delirium.load_text_list(deck_location)

        myhand = Hand()

        myhand.draw_starting_hand(gb_delirium)

        self.assertEqual(len(myhand.cards), 7)





