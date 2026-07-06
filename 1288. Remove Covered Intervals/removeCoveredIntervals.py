from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Enumeration: O(n^2) time, O(n) space

        n = len(intervals)
        is_covered = [False] * n
        for i in range(n):
            a, b = intervals[i]
            for j in range(n):
                if i == j:
                    continue
                c, d = intervals[j]
                if c <= a and b <= d:
                    is_covered[i] = True
        return is_covered.count(False)
