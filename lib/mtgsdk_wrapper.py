from mtgsdk import Card


def get_card(cardname):
    card = Card.where(name='"{}"'.format(cardname)).all()

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

    card_type = card.type
    card_type = card_type.split()

    for item in card_type:
        if item in types:
            type_list.append(item)

    return type_list


class CardMock(object):
    def __init__(self, **kwargs):
        self.name = None
        self.type = None
        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            elif key == 'type':
                self.type = value



