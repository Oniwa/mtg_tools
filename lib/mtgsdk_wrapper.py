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

    type = card.type
    type = type.split()

    for item in type:
        if item in types:
            type_list.append(item)

    return type_list



