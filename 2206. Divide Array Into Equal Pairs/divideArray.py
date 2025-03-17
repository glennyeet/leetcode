from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Hash set: O(n) time, O(n) space, where
        # n is the size of nums

        unpaired_nums = set()
        for num in nums:
            if num not in unpaired_nums:
                unpaired_nums.add(num)
            else:
                unpaired_nums.remove(num)
        return len(unpaired_nums) == 0
