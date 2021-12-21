class Solution:
    def maximalRectangle(self, matrix) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        # presum the grid
        grid = [[0 for c in range(cols)] for r in range(rows)]
        grid = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            pre_sum = 0
            for c in range(cols):
                if matrix[r][c] == '0':
                    pre_sum = 0
                else:
                    pre_sum += 1
                grid[r][c] = pre_sum

        # iterate and find largest
        max_rec = 0
        for r in range(rows):
            for c in range(cols):
                cur_cols = grid[r][c]
                cur_rows = 1
                cur_rec = cur_cols * cur_rows
                max_rec = max(max_rec, cur_rec)
                for inner in range(r + 1, rows):
                    cur_rows += 1
                    cur_cols = min(cur_cols, grid[inner][c])
                    cur_rec = cur_rows * cur_cols
                    max_rec = max(max_rec, cur_rec)
                    if cur_rec == 0: break
        return max_rec


sol = Solution()
print(sol.maximalRectangle([]))
print(sol.maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
