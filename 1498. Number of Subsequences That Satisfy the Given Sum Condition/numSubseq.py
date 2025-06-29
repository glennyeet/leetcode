from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Two Pointers: O(nlog(n)) time, O(n) space

        n = len(nums)
        mod_factor = 10**9 + 7
        sorted_nums = sorted(nums)
        right = n - 1
        subsequences = 0
        for left in range(n):
            while left <= right and sorted_nums[left] + sorted_nums[right] > target:
                right -= 1
            if left > right:
                break
            subsequences += pow(2, right - left, mod_factor)
            subsequences %= mod_factor
        return subsequences
