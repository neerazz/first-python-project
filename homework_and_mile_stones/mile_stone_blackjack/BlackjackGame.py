from homework_and_mile_stones.mile_stone_blackjack.BlackjackDeck import BlackjackDeck
from homework_and_mile_stones.mile_stone_blackjack.ComputerPlayer import ComputerPlayer
from homework_and_mile_stones.mile_stone_blackjack.Player import Player

'''
Here are the requirements:

    You need to create a simple text-based BlackJack game
    The game needs to have one player versus an automated dealer.
    The player can stand or hit.
    The player must be able to pick their betting amount.
    You need to keep track of the player's total money.
    You need to alert the player of wins, losses, or busts, etc...

And most importantly:
    You must use OOP and classes in some portion of your game.
    You can not just use functions in your game.
    Use classes to help you define the Deck and the Player's hand.
    There are many right ways to do this, so explore it well!
'''


class BlackjackGame:

    def __init__(self, player_name="Neeraj"):
        self.deck = BlackjackDeck()
        self.player1 = Player(player_name)
        self.player2 = ComputerPlayer()
        self.winner = None
        self.initialize_cards()

    def initialize_cards(self):
        self.player1.add_card(self.deck.take_card())
        self.player2.add_card(self.deck.take_card())
        self.player1.add_card(self.deck.take_card())
        self.player2.add_card(self.deck.take_card())

    def start_game(self):
        # Start game
        while self.winner is None:
            self.play_turn(self.player1)
            winner = self.get_winner()
            if winner is None:
                self.play_turn(self.player2)
        return self.winner

    def play_turn(self, player: Player):
        continue_playing = True
        while continue_playing:
            option = player.play_option()
            self.process_option(player, option)
            # When player chose to pick a card, then continue the turn
            continue_playing = option == 2
            if player.score() > 21:
                return

    def get_winner(self):
        p1_score = self.player1.score()
        p2_score = self.player2.score()
        if p1_score > 21:
            self.winner = self.player2
        elif p2_score > 21:
            self.winner = self.player1
        elif p2_score < p1_score <= 21:
            self.winner = self.player1
        elif p1_score < p2_score <= 21:
            self.winner = self.player2
        return self.winner

    def process_option(self, player: Player, option: int):
        if option == 1:
            print(f"{player} has Skipped the turn")
        elif option == 2:
            print(f"{player} has Opted to pick a card.")
            player.add_card(self.deck.take_card())


if __name__ == '__main__':
    print("Loading BlackjackGame.....")
else:
    print("Importing BlackjackGame.....")
