import unittest

from deck import Deck
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