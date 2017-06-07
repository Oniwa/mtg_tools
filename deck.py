from random import shuffle


class Deck(object):
    cards = []

    def load_text_list(self, deck_list):
        """
        Takes a text file that represents a deck of magic cards.

        Text file format is:
            number name

            IE:
            1 Emerakul, The Promised End
            4 Grim Flayer

        and stores it as a deck with a unique entry for each card.

        :param deck_list:
        :return:
        """
        self.cards = []
        card_list = []

        with open(deck_list) as f:
            for line in f:
                card_list.append(line)

        for item in card_list:
            item_list = item.split()
            item_number = int(item_list.pop(0))
            item_name = ' '.join(item_list)

            for _ in range(item_number):
                self.cards.append(item_name)

    def size(self):
        return len(self.cards)

    def shuffle_deck(self):
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def put_in_deck(self, card):
        self.cards.append(card)

    def put_cards_in_graveyard(self, number, graveyard):
        for _ in range(number):
            graveyard.append(self.draw())
