from functools import cache
from math import inf


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Top-down DP: O(n) time, O(n) space

        n = len(days)

        @cache
        def get_min_cost(days_index: int) -> int:
            if days_index == n:
                return 0
            min_cost = inf
            new_days_index = days_index
            for duration, cost in zip([1, 7, 30], costs):
                while (
                    new_days_index < n
                    and days[new_days_index] < days[days_index] + duration
                ):
                    new_days_index += 1
                min_cost = min(min_cost, cost + get_min_cost(new_days_index))
            return min_cost

        return get_min_cost(0)
