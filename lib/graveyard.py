from lib import mtgsdk_wrapper


class Graveyard(object):
    def __init__(self):
        self.cards = []
        self.delirium = False

    def check_delirium(self):
        types = []

        for item in self.cards:
            temp_type = mtgsdk_wrapper.get_types(item)
            for card_type in temp_type:
                if card_type not in types:
                    types.append(card_type)

        if len(set(types)) >= 4:
            self.delirium = True
        else:
            self.delirium = False
