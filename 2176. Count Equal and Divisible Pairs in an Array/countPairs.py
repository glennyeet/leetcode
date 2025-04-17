from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Brute Force: O(n^2) time, O(1) space

        n = len(nums)
        pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j] and i * j % k == 0:
                    pairs += 1
        return pairs
