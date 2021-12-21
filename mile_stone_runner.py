from mile_stones.mile_stone_oops import Line
from mile_stones.mile_stone_oops_accounts import Accounts
from mile_stones.mile_stone_tik_tack_tow import TicTackTow

tictacktow = TicTackTow()
tictacktow.start_game()

line = Line((3, 2), (8, 10))
print(line.dist())
print(line.slope())

jose_account = Accounts('Jose', 10)
print(jose_account)
jose_account.deposit(100)
jose_account.withdraw(100)
jose_account.withdraw(200)
