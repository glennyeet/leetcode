from typing import List
from copy import deepcopy


class Solution:
    def reverseSubmatrix(
        self, grid: List[List[int]], x: int, y: int, k: int
    ) -> List[List[int]]:
        # Matrix: O(k ^ 2) time, O(m * n) space, where m is the
        # height of grid and n is the width of grid

        new_grid = deepcopy(grid)
        for i in range(k):
            for j in range(k):
                new_grid[x + i][y + j] = grid[x + k - 1 - i][y + j]
        return new_grid
