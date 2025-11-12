from typing import List
from math import gcd


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Math: O(n^2 * log(m)) time, O(1) space

        n = len(nums)
        ones = 0
        cur_gcd = 0
        for num in nums:
            ones += num == 1
            cur_gcd = gcd(cur_gcd, num)
        if ones:
            return n - ones
        elif cur_gcd != 1:
            return -1
        min_operations_to_one = float("inf")
        for i in range(n):
            cur_gcd = 0
            for j in range(i, n):
                if j - i >= min_operations_to_one:
                    break
                cur_gcd = gcd(cur_gcd, nums[j])
                if cur_gcd == 1:
                    min_operations_to_one = j - i
                    break
        return min_operations_to_one + n - 1
