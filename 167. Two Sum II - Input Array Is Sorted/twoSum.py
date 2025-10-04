from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two Pointers: O(n) time, O(1) space

        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
