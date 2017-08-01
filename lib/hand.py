class Hand(object):
    def __init__(self):
        self.cards = []

    def draw_starting_hand(self, deck):
        for _ in range(7):
            self.cards.append(deck.draw())

    def size(self):
        return len(self.cards)

    def put_in_deck(self, card, deck):
        self.cards.remove(card)
        deck.put_in_deck(card)

    def get_card_from_deck(self, card, deck):
        for item in deck.cards:
            if item.name == card.name:
                deck.cards.remove(item)
                self.cards.append(item)
                break

    def draw(self, number, deck):
        for _ in range(number):
            self.cards.append(deck.draw())

    def play(self, card, battlefield):
        for item in self.cards:
            if item.name == card.name:
                self.cards.remove(item)
                battlefield.append(item)
                break
