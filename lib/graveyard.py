from lib import mtgsdk_wrapper


class Graveyard(object):
    cards = []
    delirium = False

    def check_delirium(self):
        types = []

        for item in self.cards:
            temp_type = mtgsdk_wrapper.get_types(item)
            for type in temp_type:
                if type not in types:
                    types.append(type)

        if len(set(types)) >= 4:
            self.delirium = True
        else:
            self.delirium = False