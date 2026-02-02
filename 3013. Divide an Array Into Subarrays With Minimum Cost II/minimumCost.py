from typing import List
from sortedcontainers import SortedList


class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # B-tree + Sliding Window: O(n * log(n)) time, O(n) space

        n = len(nums)
        min_sum = float("inf")
        cur_sum = 0
        start_window = SortedList()
        for right in range(1, n):
            left = right - (dist + 1)
            if left >= 1:
                window_index = start_window.bisect_left((nums[left], left))
                if 0 <= window_index < k - 1:
                    cur_sum -= nums[left]
                    if len(start_window) >= k:
                        cur_sum += start_window[k - 1][0]
                start_window.remove((nums[left], left))
            window_index = start_window.bisect_left((nums[right], right))
            if 0 <= window_index < k - 1:
                cur_sum += nums[right]
                if len(start_window) >= k - 1:
                    cur_sum -= start_window[k - 2][0]
            start_window.add((nums[right], right))
            if left >= 0:
                min_sum = min(min_sum, cur_sum)
        min_sum += nums[0]
        return min_sum
