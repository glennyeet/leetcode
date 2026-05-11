from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        # Math: O(n * log(n)) time, O(n * log(n)) space,
        # where n is the size of nums

        answer = []
        for num in reversed(nums):
            while num:
                answer.append(num % 10)
                num //= 10
        answer.reverse()
        return answer
