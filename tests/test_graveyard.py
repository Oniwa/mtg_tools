import unittest

from lib.graveyard import Graveyard
from lib.mtgsdk_wrapper import CardMock


class TestGraveyard(unittest.TestCase):
    # noinspection PyPep8Naming
    # This warning has been suppressed because naming convention of
    # methodName and runTest is required for unittest
    def __init__(self, methodName='runTest'):
        self.swamp = CardMock(name='Swamp', type='Basic Land \u2014 Swamp')
        self.prism = CardMock(name="Prophetic Prism", type="Artifact")
        self.bolt = CardMock(name='Lightning Bolt', type='Instant')
        self.amalgam = CardMock(name='Prized Amalgam', type='Creature \u2014 '
                                                            'Zombie')
        self.ballista = CardMock(name='Walking Ballista',
                                 type='Artifact Creature \u2014 Construct')
        unittest.TestCase.__init__(self, methodName)

    def setUp(self):
        self.my_gy = Graveyard()
        self.my_gy.delirium = False
        self.my_gy.cards = []

    def tearDown(self):
        self.my_gy.delirium = False
        self.my_gy.cards = []

    def test_check_delirium_true(self):
        cards = [self.swamp,
                 self.prism,
                 self.amalgam,
                 self.bolt,
                 ]

        for item in cards:
            self.my_gy.cards.append(item)

        self.my_gy.check_delirium()

        self.assertEqual(self.my_gy.delirium, True)

    def test_check_delirium_false(self):
        cards = [self.swamp,
                 self.swamp,
                 self.amalgam,
                 self.bolt,
                 ]

        for item in cards:
            self.my_gy.cards.append(item)

        self.my_gy.check_delirium()

        self.assertEqual(self.my_gy.delirium, False)

    def test_check_delirium_multiple_types_true(self):
        cards = [self.swamp,
                 self.ballista,
                 self.swamp,
                 self.bolt,
                 ]

        for item in cards:
            self.my_gy.cards.append(item)

        self.my_gy.check_delirium()

        self.assertEqual(self.my_gy.delirium, True)
