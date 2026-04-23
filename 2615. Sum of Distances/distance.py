from typing import List
from collections import defaultdict


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Hash Table + Preix Sum: O(n) time, O(n) space

        n = len(nums)
        arr = [0] * n
        num_indices = defaultdict(list)
        for i, num in enumerate(nums):
            num_indices[num].append(i)
        for num in num_indices:
            indices = num_indices[num]
            total = 0
            for i in range(1, len(indices)):
                total += indices[i] - indices[0]
            arr[indices[0]] = total
            for i in range(1, len(indices)):
                total += (indices[i] - indices[i - 1]) * i
                total -= (indices[i] - indices[i - 1]) * (len(indices) - i)
                arr[indices[i]] = total
        return arr
