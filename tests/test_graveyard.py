import unittest

from graveyard import Graveyard


class TestGraveyard(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check_delirium_true(self):
        mygy = Graveyard()

        cards = ['Swamp',
                 'Prophetic Prism',
                 'Prized Amalgam',
                 'Lightning Bolt',
                 ]

        for item in cards:
            mygy.cards.append(item)

        mygy.check_delirium()

        self.assertEqual(mygy.delirium, True)

    def test_check_delirium_false(self):
        mygy = Graveyard()

        cards = ['Swamp',
                 'Swamp',
                 'Prized Amalgam',
                 'Lightning Bolt',
                 ]

        for item in cards:
            mygy.cards.append(item)

        mygy.check_delirium()

        self.assertEqual(mygy.delirium, False)

    def test_check_delirium_multiple_types_true(self):
        mygy = Graveyard()

        cards = ['Swamp',
                 'Walking Ballista',
                 'Swamp',
                 'Lightning Bolt',
                 ]

        for item in cards:
            mygy.cards.append(item)

        mygy.check_delirium()

        self.assertEqual(mygy.delirium, True)


