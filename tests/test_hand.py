import unittest

from deck import Deck
from hand import Hand
from mtgsdk_wrapper import get_card


class TestHand(unittest.TestCase):
    island = get_card('Island')
    mountain = get_card('Mountain')
    test_deck = Deck()
    myhand = Hand()

    def setUp(self):
        for _ in range(7):
            self.test_deck.cards.append(self.island)

        self.test_deck.cards.append(self.mountain)

    def tearDown(self):
        self.test_deck.cards = []
        self.myhand.cards = []

    def test_draw_starting_hand(self):
        deck_location = 'D:\\code\\delirium\\tests\\test_data\\delirium.txt'

        gb_delirium = Deck()

        gb_delirium.load_text_list(deck_location)

        self.myhand.draw_starting_hand(gb_delirium)

        self.assertEqual(len(self.myhand.cards), 7)


    def test_put_in_deck(self):
        self.myhand.draw_starting_hand(self.test_deck)

        self.myhand.put_in_deck(self.mountain, self.test_deck)

        self.assertNotIn(self.mountain, self.myhand.cards)
        self.assertIn(self.mountain, self.test_deck.cards)


    def test_get_card_from_deck(self):
        deck_location = 'D:\\code\\delirium\\tests\\test_data\\delirium.txt'

        card_from_deck = Deck()

        card_from_deck.load_text_list(deck_location)

        tireless = get_card('Tireless Tracker')

        self.myhand.get_card_from_deck(tireless, card_from_deck)

        test_list = []
        for item in self.myhand.cards:
            test_list.append(item.name)

        self.assertIn(tireless.name, test_list)

        test_list = []
        for item in card_from_deck.cards:
            test_list.append(item.name)
        self.assertNotIn(tireless.name, test_list)


    def test_play(self):
        battlefield = []

        self.myhand.get_card_from_deck(self.mountain, self.test_deck)

        self.myhand.play(self.mountain, battlefield)

        self.assertIn(self.mountain, battlefield)
        self.assertNotIn(self.mountain, self.test_deck.cards)


