import unittest

from lib.deck import Deck
from lib.hand import Hand

from lib.mtgsdk_wrapper import get_card


class TestHand(unittest.TestCase):
    island = get_card('Island')
    mountain = get_card('Mountain')
    tireless = get_card('Tireless Tracker')

    test_deck = Deck()
    myhand = Hand()

    deck_location = 'D:\\code\\delirium\\tests\\test_data\\delirium.txt'
    gb_delirium = Deck()
    gb_delirium.load_text_list(deck_location)

    def setUp(self):
        for _ in range(7):
            self.test_deck.cards.append(self.island)

        self.test_deck.cards.append(self.mountain)

    def tearDown(self):
        self.test_deck.cards = []
        self.myhand.cards = []

    def test_draw_starting_hand(self):
        self.myhand.draw_starting_hand(self.gb_delirium)

        self.assertEqual(len(self.myhand.cards), 7)

        for item in self.myhand.cards:
            self.myhand.put_in_deck(item, self.gb_delirium)


    def test_put_in_deck(self):
        self.myhand.draw_starting_hand(self.test_deck)

        self.myhand.put_in_deck(self.mountain, self.test_deck)

        self.assertNotIn(self.mountain, self.myhand.cards)
        self.assertIn(self.mountain, self.test_deck.cards)


    def test_get_card_from_deck(self):
        self.myhand.get_card_from_deck(self.tireless, self.gb_delirium)

        test_list = []
        for item in self.myhand.cards:
            test_list.append(item.name)

        self.assertIn(self.tireless.name, test_list)

        test_list = []
        for item in self.gb_delirium.cards:
            test_list.append(item.name)
        self.assertNotIn(self.tireless.name, test_list)

        for item in self.myhand.cards:
            self.myhand.put_in_deck(item, self.gb_delirium)


    def test_play(self):
        battlefield = []

        self.myhand.get_card_from_deck(self.tireless, self.gb_delirium)

        self.myhand.play(self.tireless, battlefield)

        test_list = []
        for item in battlefield:
            test_list.append(item.name)
        self.assertIn(self.tireless.name, test_list)

        test_list = []
        for item in self.gb_delirium.cards:
            test_list.append(item.name)
        self.assertNotIn(self.tireless.name, test_list)

        for item in self.myhand.cards:
            self.myhand.put_in_deck(item, self.gb_delirium)

