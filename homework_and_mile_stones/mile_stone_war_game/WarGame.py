'''
https://en.wikipedia.org/wiki/War_(card_game)
Uses a 52-card Skat pack for 2 players with cards ranking in the natural order.
One player plays with the red suits and the other with the black suits.
Players get 26 cards each face down.
They turn over their top cards at the same time and the higher card wins.
    The player who has the highest card, keeps both the card.
    If the cards are equal, players turn the next card and the winner takes all four cards.
The player with the most cards at the end wins.
'''

from homework_and_mile_stones.mile_stone_war_game.BlackjackDeck import BlackjackDeck
from homework_and_mile_stones.mile_stone_war_game.Player import Player


class Game:
    deck = []
    player1 = None
    player2 = None
    winner = None
    turn = 1

    def __init__(self, p1_name="Player1", p2_name="Player2"):
        self.create_players(p1_name, p2_name)
        self.create_deck()

    def create_deck(self):
        self.deck = BlackjackDeck()

    def start_game(self):
        self.create_deck()
        self.distribute_cards()
        while self.winner is None:
            card1, card2 = self.player1.remove_card(), self.player2.remove_card()
            print(f"Turn {self.turn}: {card1}, \t\t {card2}")
            self.deck.add_card(card1)
            self.deck.add_card(card2)
            if card1.rank < card2.rank:
                # Player 2 wins, the turn
                self.give_cards_to_player(self.player2)
            elif card1.rank > card2.rank:
                # Player 1 wins, the turn
                self.give_cards_to_player(self.player1)

            self.check_winner()
            self.turn += 1

        return self.winner

    def distribute_cards(self):
        while self.deck.has_cards():
            self.player1.add_card(self.deck.take_card())
            self.player2.add_card(self.deck.take_card())

    def create_players(self, p1_name, p2_name):
        self.player1 = Player(p1_name)
        self.player2 = Player(p2_name)

    def give_cards_to_player(self, player: Player):
        while len(self.deck.cards) > 0:
            player.add_card(self.deck.cards.pop())

    def check_winner(self):
        print(
            f"Checking Winner.......\t Player 1 Cards : {len(self.player1.cards)}\tPlayer 2 Cards : {len(self.player2.cards)}")
        if not self.player1.has_cards():
            # Player 1 has no more cards, So player 2 Wins.
            self.winner = self.player2
        elif not self.player2.has_cards():
            # Player 2 has no more cards, So player 1 Wins.
            self.winner = self.player1


if __name__ == '__main__':
    print("Loading Game.....")
else:
    print("Importing Game.....")
