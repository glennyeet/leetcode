from typing import List
from math import sqrt


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Square Root Decomposition: O((n + q) * √n + q * log(m)) time,
        # O(√n + q) space, where q is the size of queries and m is mod_factor

        n = len(nums)
        mod_factor = 10**9 + 7
        block_size = int(sqrt(n))
        groups = [[] for _ in range(block_size)]
        processed_nums = nums.copy()
        for l, r, k, v in queries:
            if k < block_size:
                groups[k].append((l, r, v))
            else:
                idx = l
                while idx <= r:
                    processed_nums[idx] = processed_nums[idx] * v % mod_factor
                    idx += k
        d = n + block_size
        diff = [1] * d
        for i in range(1, block_size):
            if not groups[i]:
                continue
            diff = [1] * d
            for l, r, v in groups[i]:
                diff[l] = diff[l] * v % mod_factor
                next_multiple_index = ((r - l) // i + 1) * i + l
                diff[next_multiple_index] = (
                    diff[next_multiple_index]
                    * pow(v, mod_factor - 2, mod_factor)
                    % mod_factor
                )
            for j in range(i, n):
                diff[j] = diff[j] * diff[j - i] % mod_factor
            for j in range(n):
                processed_nums[j] = processed_nums[j] * diff[j] % mod_factor
        xor_sum = 0
        for num in processed_nums:
            xor_sum ^= num
        return xor_sum
