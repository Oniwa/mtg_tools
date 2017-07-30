import unittest

from lib.graveyard import Graveyard

from lib.mtgsdk_wrapper import get_card


class TestGraveyard(unittest.TestCase):
    swamp = get_card('Swamp')
    prism = get_card('Prophetic Prism')
    bolt = get_card('Lightning Bolt')
    amalgam = get_card('Prized Amalgam')
    ballista = get_card('Walking Ballista')

    def setUp(self):
        self.mygy = Graveyard()

    def tearDown(self):
        self.mygy.delirium = False
        self.mygy.cards = []

    def test_check_delirium_true(self):
        cards = [self.swamp,
                 self.prism,
                 self.amalgam,
                 self.bolt,
                 ]

        for item in cards:
            self.mygy.cards.append(item)

        self.mygy.check_delirium()

        self.assertEqual(self.mygy.delirium, True)

    def test_check_delirium_false(self):
        cards = [self.swamp,
                 self.swamp,
                 self.amalgam,
                 self.bolt,
                 ]

        for item in cards:
            self.mygy.cards.append(item)

        self.mygy.check_delirium()

        self.assertEqual(self.mygy.delirium, False)

    def test_check_delirium_multiple_types_true(self):
        cards = [self.swamp,
                 self.ballista,
                 self.swamp,
                 self.bolt,
                 ]

        for item in cards:
            self.mygy.cards.append(item)

        self.mygy.check_delirium()

        self.assertEqual(self.mygy.delirium, True)
