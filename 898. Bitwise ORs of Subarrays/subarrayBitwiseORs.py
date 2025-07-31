from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # Bit Manipulation + Bottom-up DP: O(nlog(a)) time,
        # O(nlog(a)) space, where n is the size of arr and 
        # a is the number of bits of max(arr)

        subarray_ors = set()
        cur_ors = set()
        for num in arr:
            new_ors = set([num])
            for cur_or in cur_ors:
                new_ors.add(num | cur_or)
            cur_ors = new_ors
            subarray_ors |= cur_ors
        return len(subarray_ors)
