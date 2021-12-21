class TicTackTow:

    def __init__(self):
        self.grid = [[' '] * 3 for _ in range(3)]
        self.rows = [0] * 3
        self.cols = [0] * 3
        self.diagonal = [0] * 2

    def print_grid(self):
        for row in self.grid:
            print(row)

    def board_completed(self):
        for count in self.rows:
            if abs(count) == 3: return True
        for count in self.cols:
            if abs(count) == 3: return True
        for count in self.diagonal:
            if abs(count) == 3: return True
        return False

    def play(self, user, row, col):
        counter = -1 if user == 0 else 1
        if row in range(0, len(self.grid)) and col in range(0, len(self.grid[0])):
            if self.grid[row][col] == ' ':
                self.rows[row] += counter
                self.cols[col] += counter
                if row == col: self.diagonal[0] += counter
                if row + col == 3: self.diagonal[1] += counter
                self.grid[row][col] = user
                self.print_grid()
            else:
                print(f"The row : {row} and col : {col} is already taken.")
                print("Select a valid chose:")
        else:
            print(f"Input should be with in range : {len(self.grid)}")
            print("Select a valid chose:")
        return user if self.board_completed() else None

    def start_game(self):
        user = 0
        user_input = input("Select your option:")
        while True:
            split = user_input.split()
            row, col = int(split[0]), int(split[1])
            if isinstance(row, int) and isinstance(col, int):
                winner = self.play(user, row, col)
                if winner == user:
                    print(f"Player {user} won the game.")
                    break
                user ^= 1
                user_input = input("Select your option:")
            else:
                print("Enter valid number with in 3 as row and col followed by space.")
