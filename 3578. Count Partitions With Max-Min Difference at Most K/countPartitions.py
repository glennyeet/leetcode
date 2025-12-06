from typing import List
from collections import deque


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # Bottom-up DP + Queue + Sliding Window: O(n) time, O(n) space

        n = len(nums)
        mod_factor = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        min_deque = deque()
        max_deque = deque()
        cur_partitions = 1
        left = 0
        for right in range(n):
            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                cur_partitions = (cur_partitions - dp[left]) % mod_factor
                left += 1
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            dp[right + 1] = cur_partitions
            cur_partitions = (cur_partitions + dp[right + 1]) % mod_factor
        return dp[n]
