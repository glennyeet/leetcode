from typing import List
from collections import Counter


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # Hash Table: O(k * log(k) * (n - k)) time, O(n) space

        n = len(nums)
        answer = []
        for i in range(n - k + 1):
            nums_counter = Counter(nums[i : i + k])
            top_x_nums = sorted(
                nums_counter.items(), key=lambda x: (x[1], x[0]), reverse=True
            )
            x_sum = 0
            for num, count in top_x_nums[:x]:
                x_sum += num * count
            answer.append(x_sum)
        return answer
