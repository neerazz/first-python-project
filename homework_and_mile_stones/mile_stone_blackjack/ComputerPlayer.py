from homework_and_mile_stones.mile_stone_blackjack.Player import Player


class ComputerPlayer(Player):

    def __init__(self, name="System"):
        super().__init__(name)

    def play_option(self):
        cur_score = self.score()
        if cur_score <= 11:
            # Chose to Pick a card.
            return 2
        elif 19 < cur_score < 21:
            # If pick any card can result in greater than 21. Then, End the Turn
            return 0
        else:
            # Skip
            return 1


if __name__ == '__main__':
    print("Loading Blackjack Computer Player.....")
else:
    print("Importing Blackjack Computer Player.....")
