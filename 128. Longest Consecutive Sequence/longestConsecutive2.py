from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space, where n is the size of nums

        unique_nums = set(nums)
        max_sequence_length = 0
        for num in unique_nums:
            if num - 1 in unique_nums:
                continue
            sequence_length = 0
            cur_num = num
            while cur_num in unique_nums:
                sequence_length += 1
                cur_num += 1
            max_sequence_length = max(max_sequence_length, sequence_length)
        return max_sequence_length
