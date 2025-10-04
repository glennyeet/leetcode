from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Greedy + Two Pointers: O(n) time, O(1) space

        n = len(height)
        left = 0
        right = n - 1
        max_water = 0
        while left < right:
            while left < right and height[left] <= height[right]:
                max_water = max(
                    max_water, (right - left) * min(height[left], height[right])
                )
                left += 1
            while left < right and height[left] > height[right]:
                max_water = max(
                    max_water, (right - left) * min(height[left], height[right])
                )
                right -= 1
        return max_water
