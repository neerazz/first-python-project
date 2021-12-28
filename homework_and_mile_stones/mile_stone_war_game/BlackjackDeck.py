import random

from homework_and_mile_stones.mile_stone_war_game.Card import Card


class BlackjackDeck:
    rank_char_dic = {}

    def __init__(self):
        self.cards = []
        self.generate_dic()
        # Generate 52 cards.
        for i in range(1, 14):
            # Loop from 1-13. 1 -> A, 2-10, 11 -> J, 12 -> Q, 13 -> K
            char = self.rank_char_dic[i]
            self.add_card(Card("Red-Heart   ", char, i))
            self.add_card(Card("Red-Dimond  ", char, i))
            self.add_card(Card("Black-Spades", char, i))
            self.add_card(Card("Black-Club  ", char, i))

        random.shuffle(self.cards)

    def take_card(self) -> Card:
        if self.has_cards():
            return self.cards.pop(0)
        else:
            print("No more cards to Pick")

    def add_card(self, card: Card):
        self.cards.append(card)

    def generate_dic(self):
        self.rank_char_dic = {n: str(n) for n in range(2, 11)}
        self.rank_char_dic[1] = "A"
        self.rank_char_dic[11] = "J"
        self.rank_char_dic[12] = "Q"
        self.rank_char_dic[13] = "K"

    def has_cards(self) -> bool:
        return len(self.cards) > 0


if __name__ == "__main__":
    print("Initializing BlackjackDeck...")
else:
    print("Importing BlackjackDeck...")
