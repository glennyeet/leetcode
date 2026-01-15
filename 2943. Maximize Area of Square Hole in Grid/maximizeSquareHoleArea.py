from typing import List


class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:
        # Sorting: O(n * log(n) + m * log(m)) time, O(n + m) space

        sorted_hbars = sorted(hBars)
        sorted_vbars = sorted(vBars)

        def find_max_consecutive_bar_removals(bars: list[int]) -> int:
            max_streak = 1
            cur_streak = 1
            for i, j in zip(bars, bars[1:]):
                if i + 1 == j:
                    cur_streak += 1
                else:
                    max_streak = max(max_streak, cur_streak)
                    cur_streak = 1
            else:
                max_streak = max(max_streak, cur_streak)
            return max_streak

        return (
            min(
                find_max_consecutive_bar_removals(sorted_hbars),
                find_max_consecutive_bar_removals(sorted_vbars),
            )
            + 1
        ) ** 2
