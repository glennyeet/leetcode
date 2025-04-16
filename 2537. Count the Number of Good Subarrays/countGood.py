from typing import List
from collections import Counter


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Sliding Window: O(n) time, O(n) space

        n = len(nums)
        pairs = 0
        good_subarrays = 0
        counter = Counter()
        left = 0
        for right in range(n):
            pairs += counter[nums[right]]
            counter[nums[right]] += 1
            while pairs >= k:
                counter[nums[left]] -= 1
                pairs -= counter[nums[left]]
                left += 1
            good_subarrays += left
        return good_subarrays
