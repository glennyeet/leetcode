from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Run-length encoding: O(n) time, O(n) space, where n is the
        # size of nums

        streaks = [0]
        max_size = 0
        for i, num in enumerate(nums):
            if i > 0 and num != nums[i - 1]:
                streaks.append(0)
            streaks[-1] += 1
            if num:
                max_size = max(max_size, streaks[-1])
        total_streaks = len(streaks)
        if total_streaks == 1 and nums[0]:
            max_size -= 1
        elif total_streaks > 1:
            if nums[0]:
                start = 0
            else:
                start = 1
            for i in range(start, total_streaks - 2, 2):
                if streaks[i + 1] == 1:
                    max_size = max(max_size, streaks[i] + streaks[i + 2])
        return max_size
