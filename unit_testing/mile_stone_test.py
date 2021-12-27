import unittest

from homework_and_mile_stones.mile_stone_blackjack.BlackjackGame import BlackjackGame
from homework_and_mile_stones.mile_stone_oops import Line
from homework_and_mile_stones.mile_stone_war_game.WarGame import Game


class MyTestCase(unittest.TestCase):

    def test_distance(self):
        line = Line((3, 2), (8, 10))
        self.assertAlmostEqual(line.dist(), 9.433, delta=0.001)

    def test_slope(self):
        line = Line((3, 2), (8, 10))
        self.assertEqual(line.slope(), 1.6)

    def test_war_game(self):
        game = Game()
        self.assertIsNotNone(game.start_game())

    def test_blackjack_game(self):
        blackjack = BlackjackGame()
        winner = blackjack.start_game()
        self.assertIsNotNone(winner)


if __name__ == '__main__':
    unittest.main()
