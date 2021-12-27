from homework_and_mile_stones.homework_errors_and_exceptions import problem1
from homework_and_mile_stones.homework_errors_and_exceptions import problem2
from homework_and_mile_stones.mile_stone_blackjack.BlackjackGame import BlackjackGame
from homework_and_mile_stones.mile_stone_oops import Line
from homework_and_mile_stones.mile_stone_tik_tack_tow import TicTackTow
from homework_and_mile_stones.mile_stone_war_game.WarGame import Game

# Blackjack Game
blackjack = BlackjackGame()
print(f"Winner is : {blackjack.start_game()}")

# WAR Game
game = Game()
print(f"Winner is : {game.start_game()}")

# Requires User Input
tictacktow = TicTackTow()
tictacktow.start_game()

line = Line((3, 2), (8, 10))
print(line.dist())
print(line.slope())

# jose_account = Accounts('Jose', 10)
# print(jose_account)
# jose_account.deposit(100)
# jose_account.withdraw(100)
# jose_account.withdraw(200)

problem1([1, 2, 3])
problem1(["word1", 'c2'])

problem2(10, 20)
problem2(20, 0)
