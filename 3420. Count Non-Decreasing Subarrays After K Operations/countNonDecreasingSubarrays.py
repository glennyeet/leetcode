from collections import deque
from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # Deque + Sliding Window: O(n) time, O(n) space

        n = len(nums)
        non_decreasing_subarrays = 0
        cur_k = k
        window_head_indices = deque()
        r = n - 1
        for l in reversed(range(n)):
            while window_head_indices and nums[window_head_indices[0]] < nums[l]:
                cur_head = window_head_indices.popleft()
                if window_head_indices:
                    next_head = window_head_indices[0]
                else:
                    next_head = r + 1
                cur_k -= (next_head - cur_head) * (nums[l] - nums[cur_head])
            window_head_indices.appendleft(l)
            while cur_k < 0:
                cur_k += nums[window_head_indices[-1]] - nums[r]
                if window_head_indices[-1] == r:
                    window_head_indices.pop()
                r -= 1
            non_decreasing_subarrays += r - l + 1
        return non_decreasing_subarrays
