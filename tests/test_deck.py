import unittest

from delirium import get_card

class TestDeck(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_card(self):
        card = get_card('Noxious Gearhulk', 'kld')

        self.assertEqual(card.name, 'Noxious Gearhulk')