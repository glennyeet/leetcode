from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        # Greedy + Bit Manipulation: O(n + k) time, O(1) space, where n is the 
        # size of nums

        mod_factor = 10**9 + 7
        bit_count = [0] * 32
        for num in nums:
            for bit in range(32):
                if num >> bit & 1:
                    bit_count[bit] += 1
        max_sum_of_squares = 0
        for _ in range(k):
            new_num = 0
            for bit in range(32):
                if bit_count[bit]:
                    new_num |= 1 << bit
                    bit_count[bit] -= 1
            max_sum_of_squares = (max_sum_of_squares + new_num**2) % mod_factor
        return max_sum_of_squares
