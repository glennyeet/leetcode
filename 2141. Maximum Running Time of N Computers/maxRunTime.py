from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # Binary Search: O(n * log(b)) time, O(1) space, where 
        # b is the max value in batteries

        left = 1
        right = sum(batteries) // n

        def can_run_computers(running_time: int) -> bool:
            available_power = 0
            for capacity in batteries:
                available_power += min(capacity, running_time)
            return available_power >= n * running_time

        while left < right:
            mid = (left + right + 1) // 2
            if can_run_computers(mid):
                left = mid
            else:
                right = mid - 1
        return left
