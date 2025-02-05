class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # One-pass: O(n) time, O(1) space

        n = len(nums)
        max_strictly_increasing = 1
        max_strictly_decreasing = 1
        strictly_increasing = 1
        strictly_decreasing = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                strictly_increasing += 1
                max_strictly_increasing = max(
                    max_strictly_increasing, strictly_increasing
                )
                strictly_decreasing = 1
            elif nums[i - 1] > nums[i]:
                strictly_decreasing += 1
                max_strictly_decreasing = max(
                    max_strictly_decreasing, strictly_decreasing
                )
                strictly_increasing = 1
            else:
                strictly_increasing = 1
                strictly_decreasing = 1
        return max(max_strictly_increasing, max_strictly_decreasing)
