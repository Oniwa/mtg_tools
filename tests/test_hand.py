import unittest

from lib.deck import Deck
from lib.hand import Hand
from lib.mtgsdk_wrapper import CardMock


class TestHand(unittest.TestCase):
    # noinspection PyPep8Naming
    # This warning has been suppressed because naming convention of
    # methodName and runTest is required for unittest
    def __init__(self, methodName='runTest'):
        self.island = CardMock(name='Island', type='')
        self.mountain = CardMock(name='Mountain', type='')
        self.tireless = CardMock(name='Tireless Tracker', type='')

        self.test_deck = Deck()
        self.my_hand = Hand()

        deck_location = 'D:\\code\\delirium\\tests\\test_data\\delirium.txt'
        self.gb_delirium = Deck()
        self.gb_delirium.load_text_list(deck_location)

        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        for _ in range(7):
            self.test_deck.cards.append(self.island)

        self.test_deck.cards.append(self.mountain)
        self.my_hand.cards = []

    def tearDown(self):
        self.test_deck.cards = []
        self.my_hand.cards = []

    def test_draw_starting_hand(self):
        self.my_hand.draw_starting_hand(self.gb_delirium)

        self.assertEqual(len(self.my_hand.cards), 7)

        for item in self.my_hand.cards:
            self.my_hand.put_in_deck(item, self.gb_delirium)

    def test_put_in_deck(self):
        self.my_hand.draw_starting_hand(self.test_deck)

        self.my_hand.put_in_deck(self.mountain, self.test_deck)

        self.assertNotIn(self.mountain, self.my_hand.cards)
        self.assertIn(self.mountain, self.test_deck.cards)

    def test_get_card_from_deck(self):
        self.my_hand.get_card_from_deck(self.tireless, self.gb_delirium)

        test_list = []
        for item in self.my_hand.cards:
            test_list.append(item.name)

        self.assertIn(self.tireless.name, test_list)

        test_list = []
        for item in self.gb_delirium.cards:
            test_list.append(item.name)
        self.assertNotIn(self.tireless.name, test_list)

        for item in self.my_hand.cards:
            self.my_hand.put_in_deck(item, self.gb_delirium)

    def test_play(self):
        battlefield = []

        self.my_hand.get_card_from_deck(self.tireless, self.gb_delirium)

        self.my_hand.play(self.tireless, battlefield)

        test_list = []
        for item in battlefield:
            test_list.append(item.name)
        self.assertIn(self.tireless.name, test_list)

        test_list = []
        for item in self.gb_delirium.cards:
            test_list.append(item.name)
        self.assertNotIn(self.tireless.name, test_list)

        for item in self.my_hand.cards:
            self.my_hand.put_in_deck(item, self.gb_delirium)
