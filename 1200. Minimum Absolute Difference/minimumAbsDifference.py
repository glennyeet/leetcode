from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Sorting: O(n * log(n)) time, O(n) space

        n = len(arr)
        min_abs_diff = float("inf")
        pairs = []
        sorted_arr = sorted(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                a = sorted_arr[i]
                b = sorted_arr[j]
                abs_diff = abs(b - a)
                if abs_diff < min_abs_diff:
                    min_abs_diff = abs_diff
                    pairs = [[a, b]]
                elif abs_diff == min_abs_diff:
                    pairs.append([a, b])
                else:
                    break
        return pairs
