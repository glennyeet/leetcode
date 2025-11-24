from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # Bit Manipulation: O(n) time, O(n) space, where n
        # is the size of nums

        answer = []
        num = 0
        for bit in nums:
            num = num << 1 | bit
            answer.append(num % 5 == 0)
        return answer
