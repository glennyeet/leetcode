from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # Hash Table: O(n) time, O(n) space, where n is the
        # size of nums

        unique_nums = set()
        duplicate_nums = []
        for num in nums:
            if num in unique_nums:
                duplicate_nums.append(num)
            else:
                unique_nums.add(num)
            if len(duplicate_nums) == 2:
                break
        return duplicate_nums
