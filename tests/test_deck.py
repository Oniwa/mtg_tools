import unittest

from deck import Deck

from delirium import get_card

class TestDeck(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_card(self):
        card = get_card('Noxious Gearhulk', 'kld')

        self.assertEqual(card.name, 'Noxious Gearhulk')

    def test_load_text_list(self):
        card_list = [
            'Emrakul, the Promised End',
            'Grim Flayer',
            'Grim Flayer',
            'Grim Flayer',
            'Grim Flayer',
            'Ishkanah, Grafwidow',
            'Ishkanah, Grafwidow',
            'Ishkanah, Grafwidow',
            'Kalitas, Traitor of Ghet',
            'Kalitas, Traitor of Ghet',
            'Mindwrack Demon',
            'Mindwrack Demon',
            'Tireless Tracker',
            'Liliana, the Last Hope',
            'Liliana, the Last Hope',
            'Liliana, the Last Hope',
            'Liliana, the Last Hope',
            'Dead Weight',
            'Grapple with the Past',
            'Grapple with the Past',
            'Grasp of Darkness',
            'Grasp of Darkness',
            'Grasp of Darkness',
            'Grasp of Darkness',
            'Murder',
            'Murder',
            'Noxious Gearhulk',
            "Pilgrim's Eye",
            "Pilgrim's Eye",
            'Ruinous Path',
            'Traverse the Ulvenwald',
            'Traverse the Ulvenwald',
            'Traverse the Ulvenwald',
            'Traverse the Ulvenwald',
            'Vessel of Nascency',
            'Vessel of Nascency',
            'Vessel of Nascency',
            'Blooming Marsh',
            'Blooming Marsh',
            'Blooming Marsh',
            'Blooming Marsh',
            'Evolving Wilds',
            'Forest',
            'Forest',
            'Forest',
            'Forest',
            'Forest',
            'Forest',
            'Forest',
            'Hissing Quagmire',
            'Hissing Quagmire',
            'Hissing Quagmire',
            'Hissing Quagmire',
            'Swamp',
            'Swamp',
            'Swamp',
            'Swamp',
            'Swamp',
            'Swamp',
            'Swamp',
        ]

        deck_location = 'D:\\code\\delirium\\tests\\test_data\\delirium.txt'

        deck_load_test = Deck()

        deck_load_test.load_text_list(deck_location)
        self.maxDiff = None
        self.assertCountEqual(deck_load_test.cards, card_list)

    def test_draw(self):
        deck_location = 'D:\\code\\delirium\\tests\\test_data\\delirium.txt'

        deck_draw_test = Deck()

        deck_draw_test.load_text_list(deck_location)

        deck_draw_test.draw()

        self.assertEqual(len(deck_draw_test.cards), 59)

    def test_put_in_deck(self):
        test_deck = Deck()

        test_deck.put_in_deck('Island')

        self.assertIn('Island', test_deck.cards)
