from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Array: O(n) time, O(1) space

        n = len(nums)
        if n == 1:
            return 0
        zero_index = nums.index(0)
        is_ascending = True
        is_descending = True
        for i in range(1, n):
            num = nums[(zero_index + i) % n]
            if num != i:
                is_ascending = False
            if num != n - i:
                is_descending = False
            if not is_ascending and not is_descending:
                return -1
        if is_ascending:
            return min(zero_index, n - zero_index + 2)
        return min (n - zero_index, zero_index + 2)