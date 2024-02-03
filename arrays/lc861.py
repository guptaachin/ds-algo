from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        if grid == None:
            return 0
        num_rows, num_cols = len(grid), len(grid[0])
        # 1. Flip the row with MSB = 0. 0111 flipped 1000. 1000 is still greater than 0111
        for r in range(num_rows):
            if grid[r][0] == 0:
                self.flip_rows(grid, r, (num_rows, num_cols))
        # 2. Flip the columns from # of 1s < # of zeros. Do not flip if they are equal
        for c in range(1, num_cols):
            sum_ = 0
            for r in range(num_rows):
                sum_ += grid[r][c]
            if sum_ < num_rows/2:
                self.flip_cols(grid, c, (num_rows, num_cols))
        final_sum = 0
        # 3. Calculate the binary sum of matrix where each row is a binary num.
        for r in range(num_rows):
            per_row_sum = self.change_binary_to_decimal(grid[r])
            final_sum += per_row_sum
        return final_sum

    def flip_rows(self, grid: List[List[int]], row_to_flip: int, shape) -> None:
        m, n = shape[0], shape[1]
        for c in range(n):
            if grid[row_to_flip][c] == 0:
                grid[row_to_flip][c] = 1
            else:
                grid[row_to_flip][c] = 0

    def flip_cols(self, grid: List[List[int]], col_to_flip: int, shape) -> None:
        m, n = shape[0], shape[1]
        for r in range(m):
            if grid[r][col_to_flip] == 0 :
                grid[r][col_to_flip] = 1
            else:
                grid[r][col_to_flip] = 0

    def change_binary_to_decimal(self, bin_list: List[int]):
        sum_ = 0
        size = len(bin_list)
        for i, b in enumerate(bin_list):
            sum_ += ((2 ** (size - 1 - i)) * b)
        return sum_

