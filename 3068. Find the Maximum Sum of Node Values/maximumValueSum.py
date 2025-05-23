from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        xor_increase = []
        for num in nums:
            xor_increase.append((num ^ k) - num)
        xor_increase.sort(reverse=True)
        max_sum = sum(nums)
        for i in range(0, n, 2):
            if i + 1 == n:
                continue
            increase1 = xor_increase[i]
            increase2 = xor_increase[i + 1]
            if increase1 + increase2 > 0:
                max_sum += increase1 + increase2
        return max_sum
