from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Brute Force: O(n^3) time, O(1) space

        n = len(nums)
        min_distance = float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        min_distance = min(
                            min_distance, abs(i - j) + abs(j - k) + abs(k - i)
                        )
        if min_distance == float("inf"):
            return -1
        return min_distance
