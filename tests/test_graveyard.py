import unittest

from lib.graveyard import Graveyard
from mtgsdk import Card
from lib.mtgsdk_wrapper import get_card


class TestGraveyard(unittest.TestCase):
    swamp = Card()
    swamp.name = 'Swamp'
    swamp.type = 'Basic Land \u2014 Swamp'

    prism = Card()
    prism.name = "Prophetic Prism"
    prism.type = "Artifact"

    bolt = Card()
    bolt.name = 'Lightning Bolt'
    bolt.type = 'Instant'

    amalgam = Card()
    amalgam.name = 'Prized Amalgam'
    amalgam.type = 'Creature \u2014 Zombie'

    ballista = Card()
    ballista.name = 'Walking Ballista'
    ballista.type = 'Artifact Creature \u2014 Construct'


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
