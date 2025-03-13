from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Line sweep + Binary search: O((q + n)log(q)) time, O(n) space

        n = len(nums)
        q = len(queries)
        l = 0
        r = q + 1

        def is_zero_array(query_end_index: int) -> bool:
            decrements = [0] * (n + 1)
            for l, r, val in queries[:query_end_index]:
                decrements[l] += val
                decrements[r + 1] -= val
            total_decrement = 0
            for i in range(n):
                total_decrement += decrements[i]
                if total_decrement < nums[i]:
                    return False
            return True

        while l < r:
            mid = (l + r) // 2
            if is_zero_array(mid):
                r = mid
            else:
                l = mid + 1
        if l > q:
            return -1
        else:
            return l
