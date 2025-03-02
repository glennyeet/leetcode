from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        # Two pointers: O(m + n) time, O(m + n) space

        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        result = []
        while i < m and j < n:
            _id1, val1 = nums1[i]
            _id2, val2 = nums2[j]
            cur_id = min(_id1, _id2)
            result_val = 0
            if cur_id == _id1:
                result_val += val1
                i += 1
            if cur_id == _id2:
                result_val += val2
                j += 1
            result.append([cur_id, result_val])
        while i < m:
            _id, val = nums1[i]
            result.append([_id, val])
            i += 1
        while j < n:
            _id, val = nums2[j]
            result.append([_id, val])
            j += 1
        return result
