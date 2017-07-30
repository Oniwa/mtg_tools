import unittest

from mtgsdk_wrapper import get_card, get_types


class TestMtgsdkWrapper(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_card_lightning_bolt(self):
        test_card = get_card('Lightning Bolt')

        self.assertEqual(test_card.name, 'Lightning Bolt')

    def test_get_type_lightning_bolt(self):
        test_card = get_card('Lightning Bolt')

        self.assertEqual(test_card.type, 'Instant')

    def test_get_card_walking_ballista(self):
        test_card = get_card('Walking Ballista')

        self.assertEqual(test_card.name, 'Walking Ballista')

    def test_get_type_walking_ballista(self):
        card_types = ['Artifact', 'Creature']

        test_card = get_card('Walking Ballista')
        test_list = get_types(test_card)

        self.assertEqual(len(test_list), len(card_types))
        self.assertEqual(sorted(test_list), sorted(card_types))
