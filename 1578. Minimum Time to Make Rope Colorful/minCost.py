from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Greedy: O(n) time, O(1) space

        n = len(colors)
        cur_colour = None
        min_time = 0
        streak_sum = 0
        streak_max = 0
        for i, colour in enumerate(colors):
            if colour != cur_colour:
                min_time += streak_sum - streak_max
                cur_colour = colour
                streak_sum = neededTime[i]
                streak_max = neededTime[i]
            else:
                streak_sum += neededTime[i]
                streak_max = max(streak_max, neededTime[i])
                if i == n - 1:
                    min_time += streak_sum - streak_max
        return min_time
