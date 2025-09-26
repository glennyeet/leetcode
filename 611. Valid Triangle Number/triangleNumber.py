from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Math + Two Pointers: O(n^2) time, O(n) space

        n = len(nums)
        sorted_nums = sorted(nums)
        valid_triplets = 0
        for i in reversed(range(n)):
            c = sorted_nums[i]
            left = 0
            right = i - 1
            while left < right:
                a = sorted_nums[left]
                b = sorted_nums[right]
                if a + b > c:
                    valid_triplets += right - left
                    right -= 1
                else:
                    left += 1
        return valid_triplets
