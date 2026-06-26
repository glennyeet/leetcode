from typing import List


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Prefix Sum: O(n) time, O(n) space

        n = len(nums)
        balance_freq = [0] * (2 * n + 1)
        prefix_balance = n
        balance_freq[prefix_balance] = 1
        total_subarrays = 0
        cur_subarrays = 0
        for num in nums:
            if num == target:
                cur_subarrays += balance_freq[prefix_balance]
                prefix_balance += 1
            else:
                prefix_balance -= 1
                cur_subarrays -= balance_freq[prefix_balance]
            balance_freq[prefix_balance] += 1
            total_subarrays += cur_subarrays
        return total_subarrays
