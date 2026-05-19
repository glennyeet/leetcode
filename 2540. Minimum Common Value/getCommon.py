from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Hash Table + Math: O(m + n) time, O(m + n) space, where m
        # is the size of nums1 and n is the size of nums2

        intersection = set(nums1) & set(nums2)
        if not intersection:
            return -1
        return min(intersection)
