from bisect import bisect_right
from functools import cache
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Binary Search + Top-down DP: O(n * log(n)) time, O(n) space, where n is
        # the size of intervals

        min_interval_index = {}
        for i, (l, r, weight) in enumerate(intervals):
            key = (l, r, weight)
            if key not in min_interval_index:
                min_interval_index[key] = i
        sorted_intervals = sorted(min_interval_index.keys())
        m = len(sorted_intervals)
        next_valid_interval_index = [0] * m
        for i, (_, r, _) in enumerate(sorted_intervals):
            next_valid_interval_index[i] = bisect_right(
                sorted_intervals, (r, float("inf"), float("inf"))
            )

        @cache
        def dp(i: int, total_intervals: int) -> tuple[int, list[int]]:
            if i == m or total_intervals == 0:
                return (0, [])
            max_score = dp(i + 1, total_intervals)
            l, r, weight = sorted_intervals[i]
            take_score, take_indices = dp(
                next_valid_interval_index[i], total_intervals - 1
            )
            take_score -= weight
            take_indices = sorted(take_indices + [min_interval_index[(l, r, weight)]])
            max_score = min(max_score, (take_score, take_indices))
            return max_score

        return dp(0, 4)[1]
