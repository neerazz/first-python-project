class Card:

    def __init__(self, colour, char, rank):
        self.colour = colour
        self.char = char
        self.rank = rank

    def __str__(self):
        return f"{self.char} - {self.colour}. \t Rank : {self.rank}"

    def rank(self):
        return [1, 11] if self.rank == 11 else [self.rank()]
