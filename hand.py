class Hand(object):
    cards = []

    def draw_starting_hand(self, deck):
        for _ in range(7):
            self.cards.append(deck.draw())

    def size(self):
        return len(self.cards)

    def put_in_deck(self, card, deck):
        self.cards.remove(card)
        deck.put_in_deck(card)

    def get_card_from_deck(self, card, deck):
        deck.cards.remove(card)
        self.cards.append(card)

    def draw(self, number, deck):
        for _ in range(number):
            self.cards.append(deck.draw())

