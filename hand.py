class Hand(object):
    cards = []

    def draw_starting_hand(self, deck):
        for _ in range(7):
            self.cards.append(deck.draw())
