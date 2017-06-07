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

    def test_put_in_deck(self):
        test_deck = Deck()

        for _ in range(7):
            test_deck.cards.append('Island')

        test_deck.cards.append('Mountain')

        myhand = Hand()

        myhand.draw_starting_hand(test_deck)

        myhand.put_in_deck('Mountain', test_deck)

        self.assertNotIn('Mountain', myhand.cards)
        self.assertIn('Mountain', test_deck.cards)

    def test_get_card_from_deck(self):
        test_deck = Deck()

        for _ in range(7):
            test_deck.cards.append('Island')

        test_deck.cards.append('Mountain')

        myhand = Hand()

        myhand.get_card_from_deck('Mountain', test_deck)

        self.assertIn('Mountain', myhand.cards)
        self.assertNotIn('Mountain', test_deck.cards)

    def test_play(self):
        test_deck = Deck()
        battlefield = []

        for _ in range(7):
            test_deck.cards.append('Island')

        test_deck.cards.append('Mountain')

        myhand = Hand()

        myhand.get_card_from_deck('Mountain', test_deck)

        myhand.play('Mountain', battlefield)

        self.assertIn('Mountain', battlefield)
        self.assertNotIn('Mountain', test_deck.cards)
