from math import ceil


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        min_penalty = max(nums)
        low = 1
        high = min_penalty
        while low <= high:
            max_balls = low + (high - low) // 2
            operations = 0
            for num in nums:
                operations += ceil(num / max_balls) - 1
            if operations <= maxOperations:
                min_penalty = max_balls
                high = max_balls - 1
            else:
                low = max_balls + 1
        return min_penalty
