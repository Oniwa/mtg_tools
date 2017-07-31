import unittest

from lib.graveyard import Graveyard
from lib.mtgsdk_wrapper import CardMock


class TestGraveyard(unittest.TestCase):
    swamp = CardMock(name='Swamp', type='Basic Land \u2014 Swamp')
    prism = CardMock(name="Prophetic Prism", type="Artifact")
    bolt = CardMock(name='Lightning Bolt', type='Instant')
    amalgam = CardMock(name='Prized Amalgam', type='Creature \u2014 Zombie')
    ballista = CardMock(name='Walking Ballista',
                        type='Artifact Creature \u2014 Construct')

    def setUp(self):
        self.mygy = Graveyard()
        self.mygy.delirium = False
        self.mygy.cards = []

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
