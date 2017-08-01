import unittest

from lib.mtgsdk_wrapper import get_card, get_types, CardMock


class TestMtgSdkWrapper(unittest.TestCase):

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


class TestCardMock(unittest.TestCase):
    def test_card_mock_name_only(self):
        name = CardMock(name='Lightning Bolt')

        self.assertEqual(name.name, 'Lightning Bolt')

    def test_card_mock_type_only(self):
        card_type = CardMock(type='Instant')

        self.assertEqual(card_type.type, 'Instant')

    def test_card_mock_name_and_type(self):
        card_mock = CardMock(name='Lightning Bolt', type='Instant')

        self.assertEqual(card_mock.name, 'Lightning Bolt')
        self.assertEqual(card_mock.type, 'Instant')

    def test_card_mock_undefined_arguments(self):
        undefined_args = CardMock(cmc=3, text='Ach Hans Run!')

        self.assertEqual(undefined_args.name, None)
        self.assertEqual(undefined_args.type, None)

    def test_card_mock_undefined_args_and_name_and_type(self):
        card_mock = CardMock(name='Lava Spike', type='Sorcery \u2014 Arcane',
                             cmc=1, text='Deal 3 damage to target player.')

        self.assertEqual(card_mock.name, 'Lava Spike')
        self.assertEqual(card_mock.type, 'Sorcery \u2014 Arcane')
