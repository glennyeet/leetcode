from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Bottom-up DP: O(n) time, O(1) space, where n is the
        # size of nums

        same_parities = [0, 0]
        alternating_parities = [0, 0]
        for num in nums:
            parity = num % 2
            same_parities[parity] += 1
            alternating_parities[parity] = alternating_parities[1 - parity] + 1
        return max(max(same_parities), max(alternating_parities))
