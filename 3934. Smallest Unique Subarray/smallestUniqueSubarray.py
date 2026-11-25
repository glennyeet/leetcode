from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        # Binary Search + Rolling Hash: O(n * log(n)) time, O(n) space

        n = len(nums)
        mod_factor = 10**9 + 7
        max_num = max(nums)

        def is_valid(window_len: int) -> int:
            base = max_num + 5
            base_pow = pow(base, window_len, mod_factor)
            hash_counts = Counter()
            window_hash = 0
            for right in range(n):
                window_hash = (window_hash * base + (nums[right] + 1)) % mod_factor
                left = right - window_len
                if left >= 0:
                    window_hash = (
                        window_hash - (nums[left] + 1) * base_pow
                    ) % mod_factor
                if right - window_len + 1 >= 0:
                    hash_counts[window_hash] += 1
            for count in hash_counts.values():
                if count == 1:
                    return True
            return False

        left = 1
        right = n
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left
