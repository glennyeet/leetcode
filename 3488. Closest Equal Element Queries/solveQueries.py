from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Hash Table + Binary Search: O(n + q * log(p)) time, O(n + q) space

        n = len(nums)
        q = len(queries)
        num_indices = defaultdict(list)
        for i in range(n):
            num_indices[nums[i]].append(i)
        answer = [-1] * q
        for i in range(q):
            num = nums[queries[i]]
            indices = num_indices[num]
            m = len(num_indices[num])
            if m == 1:
                continue
            indices_index = bisect_left(indices, queries[i])
            left_index = indices[(indices_index - 1) % m]
            right_index = indices[(indices_index + 1) % m]
            answer[i] = min(
                abs(queries[i] - left_index),
                n - abs(queries[i] - left_index),
                abs(queries[i] - right_index),
                n - abs(queries[i] - right_index),
            )
        return answer
