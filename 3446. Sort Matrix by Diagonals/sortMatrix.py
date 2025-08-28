from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # Simulation: O(n^2log(n)) time, O(n^2) space

        n = len(grid)
        sorted_grid = [[0] * n for _ in range(n)]
        for i0 in range(n):
            i = i0
            j = 0
            diagonal = []
            while i < n:
                diagonal.append(grid[i][j])
                i += 1
                j += 1
            diagonal.sort(reverse=True)
            i = i0
            j = 0
            for num in diagonal:
                sorted_grid[i][j] = num
                i += 1
                j += 1
        for j0 in range(1, n):
            i = 0
            j = j0
            diagonal = []
            while j < n:
                diagonal.append(grid[i][j])
                i += 1
                j += 1
            diagonal.sort()
            i = 0
            j = j0
            for num in diagonal:
                sorted_grid[i][j] = num
                i += 1
                j += 1
        return sorted_grid
