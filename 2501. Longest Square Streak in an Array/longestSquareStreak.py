from collections import Counter


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        counter = Counter(set(nums))
        max_num = max(nums)
        for num in counter:
            cur = num**2
            while cur <= max_num and cur in counter:
                counter[num] += 1
                cur **= 2
        square_streak = counter.most_common(1)[0][1]
        if square_streak == 1:
            return -1
        else:
            return square_streak
