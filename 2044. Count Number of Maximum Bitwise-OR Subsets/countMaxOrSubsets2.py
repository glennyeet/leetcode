from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Recursion: O(2^n) time, O(n) space

        n = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num

        def count_valid_subsets(i: int, cur_or: int) -> int:
            if i == n:
                return 0
            subsets = count_valid_subsets(i + 1, cur_or)
            new_or = cur_or | nums[i]
            if new_or == max_or:
                subsets += 1 + count_valid_subsets(i + 1, new_or)
            else:
                subsets += count_valid_subsets(i + 1, new_or)
            return subsets

        return count_valid_subsets(0, 0)
