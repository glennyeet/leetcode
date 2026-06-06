from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Prefix Sum: O(n) time, O(n) space, where n is the size
        # of nums

        left_sum = []
        cur_left_sum = 0
        for num in nums:
            left_sum.append(cur_left_sum)
            cur_left_sum += num
        right_sum = []
        cur_right_sum = 0
        for num in reversed(nums):
            right_sum.append(cur_right_sum)
            cur_right_sum += num
        right_sum.reverse()
        answer = []
        for left, right in zip(left_sum, right_sum):
            answer.append(abs(left - right))
        return answer
