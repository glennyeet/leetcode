from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Cantor's Diagonal Argument: O(n) time, O(n) space

        n = len(nums)
        unseen_string = []
        for i in range(n):
            if nums[i][i] == "0":
                unseen_string.append("1")
            else:
                unseen_string.append("0")
        return "".join(unseen_string)
