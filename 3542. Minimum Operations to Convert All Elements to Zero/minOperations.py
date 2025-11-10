from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Greedy + Monotonic Stack: O(n) time, O(n)
        # space, where n is the size of nums

        operations = 0
        stack = []
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if num > 0 and (not stack or num > stack[-1]):
                stack.append(num)
                operations += 1
        return operations
