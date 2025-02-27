from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # Hash set: O(n^2log(m)) time, O(n) space, where
        # m = max(arr)

        n = len(arr)
        nums_set = set(arr)
        max_length = 0
        for i in range(n - 1):
            for j in range(i + 1, n - 2):
                length = 1
                x1 = arr[i]
                x2 = arr[j]
                while x2 in nums_set:
                    length += 1
                    x1, x2 = x2, x1 + x2
                if length >= 3:
                    max_length = max(max_length, length)
        return max_length
