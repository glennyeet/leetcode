from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Greedy: O(n) time, O(1) space

        nums1_zeroes = nums1.count(0)
        nums1_sum = sum(nums1) + nums1_zeroes
        nums2_zeroes = nums2.count(0)
        nums2_sum = sum(nums2) + nums2_zeroes
        if (
            nums1_sum < nums2_sum
            and not nums1_zeroes
            or nums1_sum > nums2_sum
            and not nums2_zeroes
        ):
            return -1
        return max(nums1_sum, nums2_sum)
