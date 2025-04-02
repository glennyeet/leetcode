from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Greedy: O(n) time, O(n) space

        n = len(nums)
        max_i = [0] * n
        max_i[0] = nums[0]
        max_k = [0] * n
        max_k[-1] = nums[-1]
        for index in range(1, n):
            max_i[index] = max(max_i[index - 1], nums[index])
        for index in reversed(range(n - 1)):
            max_k[index] = max(max_k[index + 1], nums[index])
        max_value = 0
        for index in range(1, n - 1):
            max_value = max(
                max_value, (max_i[index - 1] - nums[index]) * max_k[index + 1]
            )
        return max_value
