from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Backtracking O(2^n) time, O(n) space

        n = len(nums)

        def get_xor_sum(index: int, xor_sum: int) -> int:
            if index >= n:
                return xor_sum
            return get_xor_sum(index + 1, xor_sum ^ nums[index]) + get_xor_sum(
                index + 1, xor_sum
            )

        return get_xor_sum(0, 0)
