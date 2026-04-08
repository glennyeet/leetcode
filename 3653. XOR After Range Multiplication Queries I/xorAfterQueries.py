from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Simulation + Bit Manipulation: O(q * n) time, O(n) space, where q is
        # queries and n is nums

        mod_factor = 10**9 + 7
        processed_nums = nums.copy()
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                processed_nums[idx] = (processed_nums[idx] * v) % mod_factor
                idx += k
        xor_sum = 0
        for num in processed_nums:
            xor_sum ^= num
        return xor_sum
