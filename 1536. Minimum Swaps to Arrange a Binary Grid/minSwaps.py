from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # Greedy: O(n^2) time, O(n) space

        n = len(grid)
        rightmost_one = [-1] * n
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    rightmost_one[i] = j
        min_swaps = 0
        for i in range(n):
            swaps = 0
            for j in range(n):
                if rightmost_one[j] is not None:
                    if rightmost_one[j] <= i:
                        min_swaps += swaps
                        rightmost_one[j] = None
                        break
                    else:
                        swaps += 1
            else:
                return -1
        return min_swaps
