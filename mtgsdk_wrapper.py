from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type


def get_card(cardname, setname):
    card = Card.where(set=setname).where(name=cardname).all()

    return card[0]


def get_types(card):
    type_list = []
    types = ['Artifact',
             'Creature',
             'Enchantment',
             'Instant',
             'Land',
             'Planeswalker',
             'Tribal',
             'Sorcery',
            ]

    type = card.type
    type = type.split()

    for item in type:
        if item in types:
            type_list.append(item)

    return type_list



