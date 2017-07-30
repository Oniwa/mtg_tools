import unittest

from graveyard import Graveyard
from mtgsdk_wrapper import get_card


class TestGraveyard(unittest.TestCase):
    swamp = get_card('Swamp')
    prism = get_card('Prophetic Prism')
    bolt = get_card('Lightning Bolt')
    amalgam = get_card('Prized Amalgam')
    ballista = get_card('Walking Ballista')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_delirium_true(self):
        mygy = Graveyard()

        cards = [self.swamp,
                 self.prism,
                 self.amalgam,
                 self.bolt,
                 ]

        for item in cards:
            mygy.cards.append(item)

        mygy.check_delirium()

        self.assertEqual(mygy.delirium, True)

    def test_check_delirium_false(self):
        mygy = Graveyard()

        cards = [self.swamp,
                 self.swamp,
                 self.amalgam,
                 self.bolt,
                 ]

        for item in cards:
            mygy.cards.append(item)

        mygy.check_delirium()

        self.assertEqual(mygy.delirium, False)

    def test_check_delirium_multiple_types_true(self):
        mygy = Graveyard()

        cards = [self.swamp,
                 self.ballista,
                 self.swamp,
                 self.bolt,
                 ]

        for item in cards:
            mygy.cards.append(item)

        mygy.check_delirium()

        self.assertEqual(mygy.delirium, True)


