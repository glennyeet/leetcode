from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # Prefix and Suffix Arrays: O(n) time, O(n) space

        n = len(height)
        max_left_elevations = [0]
        for i in range(n):
            max_left_elevations.append(max(max_left_elevations[-1], height[i]))
        max_right_elevations = [0]
        for i in reversed(range(n)):
            max_right_elevations.append(max(max_right_elevations[-1], height[i]))
        max_right_elevations.reverse()
        water = 0
        for i in range(1, n - 1):
            water += max(
                min(max_left_elevations[i], max_right_elevations[i]) - height[i], 0
            )
        return water
