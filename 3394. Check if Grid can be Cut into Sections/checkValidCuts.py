from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Greedy: O(nlog(n)) time, O(n) space

        x_intervals = []
        y_intervals = []
        for start_x, start_y, end_x, end_y in rectangles:
            x_intervals.append((start_x, end_x))
            y_intervals.append((start_y, end_y))
        x_intervals.sort()
        y_intervals.sort()

        def count_non_overlapping_intervals(intervals: list[tuple[int, int]]) -> int:
            non_overlapping_intervals = 0
            max_end = 0
            for start, end in intervals:
                if start >= max_end:
                    non_overlapping_intervals += 1
                max_end = max(max_end, end)
            return non_overlapping_intervals

        return (
            count_non_overlapping_intervals(x_intervals) >= 3
            or count_non_overlapping_intervals(y_intervals) >= 3
        )
