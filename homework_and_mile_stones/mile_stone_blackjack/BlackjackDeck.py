import random

from homework_and_mile_stones.mile_stone_war_game.Card import Card

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
values = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
ranks = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
         'Queen': 10, 'King': 10, 'Ace': 11}


class BlackjackDeck:

    def __init__(self):
        self.cards = []
        self.generate_cards()
        random.shuffle(self.cards)

    def generate_cards(self):
        for key, value in ranks.items():
            for suite in suits:
                self.add_card(Card(suite, key, value))

    def take_card(self) -> Card:
        return self.remove_card()

    def remove_card(self) -> Card:
        cards_len = len(self.cards)
        if cards_len > 0:
            return self.cards.pop(0)

    def add_card(self, card: Card):
        self.cards.append(card)
