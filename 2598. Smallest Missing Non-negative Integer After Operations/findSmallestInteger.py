from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainders_counter = [0] * value
        for num in nums:
            remainders_counter[num % value] += 1
        min_remainder = 0
        for i, count in enumerate(remainders_counter):
            if count < remainders_counter[min_remainder]:
                min_remainder = i
        return min_remainder + remainders_counter[min_remainder] * value
