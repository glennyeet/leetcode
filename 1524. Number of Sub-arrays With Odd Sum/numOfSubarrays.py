from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Prefix sum: O(n) time, O(1) space, where
        # n is the size of arr

        prefix_sum = 0
        odd_prefix_sums = 0
        even_prefix_sums = 0
        odd_subarrays = 0
        for num in arr:
            prefix_sum += num
            if prefix_sum % 2:
                odd_subarrays += 1 + even_prefix_sums
                odd_prefix_sums += 1
            else:
                odd_subarrays += odd_prefix_sums
                even_prefix_sums += 1
        return odd_subarrays % (10**9 + 7)
