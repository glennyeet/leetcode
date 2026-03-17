from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Greedy: O(m * n^2) time, O(n) space

        m = len(matrix)
        n = len(matrix[0])
        col_streaks = [0] * n
        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    col_streaks[j] = 0
                else:
                    col_streaks[j] += 1
            cur_streaks = sorted(col_streaks, reverse=True)
            for i, cur_streak in enumerate(cur_streaks, start=1):
                max_area = max(max_area, i * cur_streak)
        return max_area
