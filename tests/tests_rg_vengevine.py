import unittest

from lib.deck import Deck
from lib.hand import Hand
from lib.mtgsdk_wrapper import get_types

class TestGRVengevine(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gr_vengevine(self):
        # James wants to calculate how often he will get a playable hand
        # with the GR Vengevine deck.  He defines a playable hand as two
        # castable creatures, a discard outlet, at least 2 lands, and
        # 2 vengevines by turn 3.  He will start by loading his deck list.
        gr_vv = Deck()
        gr_vv.load_text_list('D:\\code\\delirium\\tests\\test_data\\'
                             'GR_vengevine.txt')

        # He knows the deck should have 60 cards in it.
        self.assertEquals(gr_vv.size(), 60)

        # James then shuffles the deck
        gr_vv.shuffle_deck()

        # Then he draws 7 cards to his hand
        my_hand = Hand()

        my_hand.draw_starting_hand(gr_vv)
        self.assertEqual(my_hand.size(), 7)
        self.assertEqual(gr_vv.size(), 53)

        # draw 3 more cards
        my_hand.draw(3, gr_vv)

        keep_hand = True

        creature_count = 0
        land_count = 0
        discard_count = 0
        vengevine_count = 0
        for card in my_hand.cards:
            types = get_types(card)
            # Check for 2 creatures that are castable in the first 3 turns.
            # Since the only creatures in the deck that are castable by
            # turn 3 are one drops we can just check converted mana cost.
            # Later we will have to make sure we have at least one red source.
            # This assumption does not count Hooting Mandrils since they usually
            # want a stocked graveyard.  Hollow Ones count because with one
            # discard outlet there is a good chance to land one on turn 3.
            if 'Land' not in types:
                if card.cmc < 3 and 'Creature' in types:
                    creature_count += 1
                elif card.name == "Hollow One":
                    creature_count += 1
                # While we are checking creatures we should check for Vengevines
                elif card.name == "Vengevine":
                    vengevine_count += 1

                # Check for discard outlets
                if 'discard ' in card.text.lower():
                    discard_count += 1

            # Since all the lands in the deck produce red mana and that is
            # all that is typically needed by turn 3 I am just checking to
            # to make sure that two lands have been drawn.
            else:
                land_count += 1

        if creature_count < 2:
            keep_hand = False

        if land_count < 2:
            keep_hand = False

        if discard_count < 1:
            keep_hand = False

        if vengevine_count < 2:
            keep_hand = False

        count = 0
        if keep_hand:
            count += 1

        print(count)
