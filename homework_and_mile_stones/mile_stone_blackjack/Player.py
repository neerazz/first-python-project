from homework_and_mile_stones.mile_stone_war_game.Card import Card


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return f"{self.name} : my score is {self.score()}"

    def play_option(self):
        while True:
            user_option = input("Select your Option:\n\t1.Skip\n\t2.Hit\n")
            try:
                return int(user_option)
            except:
                print(f"Selected an Invalid Option : {user_option}.\n Kindly provide a valid option.")

    def add_card(self, card: Card):
        self.cards.append(card)

    def score(self):
        cards_sum = 0
        a_count = 0
        # Get The score of all the cards.
        for card in self.cards:
            if card.char == 'A':
                a_count += 1
            else:
                cards_sum += card.rank

        # Find the optimal value for A.
        while a_count > 0:
            if cards_sum < 11:
                if cards_sum + a_count <= 21:
                    cards_sum += 1
                else:
                    cards_sum += 11
            else:
                cards_sum += 1
            a_count -= 1

        return cards_sum


if __name__ == '__main__':
    print("Loading Blackjack Player.....")
else:
    print("Importing Blackjack Player.....")
