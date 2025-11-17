from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # One-pass: O(n) time, O(1) space, where n is the
        # size of nums

        indices_from_last_one = float("inf")
        for bit in nums:
            if bit == 0:
                indices_from_last_one += 1
            else:
                if indices_from_last_one < k:
                    return False
                indices_from_last_one = 0
        return True
