from typing import List
from collections import Counter


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Hash map: O(n^2) time, O(n^2) space

        n = len(grid)
        counter = Counter()
        for i in range(n):
            for j in range(n):
                counter[grid[i][j]] += 1
        ans = [0, 0]
        for i in range(1, n**2 + 1):
            if counter[i] == 2:
                ans[0] = i
            elif counter[i] == 0:
                ans[1] = i
        return ans
