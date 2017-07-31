import unittest

from lib.deck import Deck

from lib.mtgsdk_wrapper import get_card


class TestDeckAPI(unittest.TestCase):
    deck_location = 'D:\\code\\delirium\\tests\\test_data\\delirium.txt'

    deck = Deck()

    deck.load_text_list(deck_location)

    def setUp(self):
        pass

    def tearDown(self):
        self.deck.shuffle_deck()

    def test_get_card(self):
        card = get_card('Noxious Gearhulk')

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

        loaded_deck = []

        for item in self.deck.cards:
            loaded_deck.append(item.name)

        self.maxDiff = None
        self.assertEqual(len(card_list), len(loaded_deck))
        self.assertEqual(sorted(card_list), sorted(loaded_deck))


    def test_draw(self):
        card = self.deck.draw()

        self.assertEqual(len(self.deck.cards), 59)

        self.deck.put_in_deck(card)


    def test_put_cards_in_graveyard(self):
        graveyard= []

        self.deck.put_cards_in_graveyard(4, graveyard)

        self.assertEqual(56, self.deck.size())
        self.assertEqual(4, len(graveyard))

        for item in graveyard:
            self.deck.put_in_deck(item)


class TestDeckUtility(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_murder(self):
        card = get_card('Murder')

        self.assertEqual(card.name, 'Murder')

    def test_claim_to_fame(self):
        card = get_card('claim')

        self.assertEqual(card.name, 'Claim')

    def test_put_in_deck(self):
        test_deck = Deck()

        test_deck.put_in_deck('Island')

        self.assertIn('Island', test_deck.cards)
