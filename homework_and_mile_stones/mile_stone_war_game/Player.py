import random

from homework_and_mile_stones.mile_stone_war_game.Card import Card


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)
        self.shuffle()

    def remove_card(self) -> Card:
        if self.has_cards():
            return self.cards.pop(0)
        else:
            print(f"{self.name} has no more cards.")

    def has_cards(self) -> bool:
        return len(self.cards) > 0

    def __str__(self):
        return f"{self.name}, I have {len(self.cards)} cards."
