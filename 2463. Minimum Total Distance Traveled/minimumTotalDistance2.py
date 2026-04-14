from typing import List
from functools import cache


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # Top-down DP: O((m + n) * l) time, O(m + n) space, where l is the max limit in
        # factory

        m = len(robot)
        n = len(factory)
        sorted_robots = sorted(robot)
        sorted_factories = sorted(factory)

        @cache
        def dp(robot_index: int, factory_index: int) -> int | float:
            if factory_index == n:
                return float("inf")
            min_dist = float("inf")
            cur_dist = 0
            for i in range(sorted_factories[factory_index][1] + 1):
                if robot_index + i >= m:
                    min_dist = min(min_dist, cur_dist)
                    break
                min_dist = min(
                    min_dist, cur_dist + dp(robot_index + i, factory_index + 1)
                )
                cur_dist += abs(
                    sorted_factories[factory_index][0] - sorted_robots[robot_index + i]
                )
            return min_dist

        return dp(0, 0)
