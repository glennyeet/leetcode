from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # Two Pointers: O(m + n) time, O(1) space

        m = len(nums1)
        n = len(nums2)
        max_pair_dist = 0
        i = 0
        j = 0
        while i < m and j < n:
            if i <= j and nums1[i] <= nums2[j]:
                max_pair_dist = max(max_pair_dist, j - i)
                j += 1
            elif i <= j:
                i += 1
            else:
                j += 1
        return max_pair_dist
