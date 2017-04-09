from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type


def get_card(cardname, setname):
    card = Card.where(set=setname).where(name=cardname).all()

    return card[0]


class Deck(object):
    cards = []

    def list_to_deck(self):
        pass

