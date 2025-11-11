from typing import List
from functools import cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Top-down DP: O(s * m * n * b) time, O(s * m * n) space,
        # where b is size of the longest string in strs

        s = len(strs)

        @cache
        def find_largest_subset_size(
            index: int, total_zeroes: int, total_ones: int
        ) -> int:
            if index == s:
                return 0
            largest_subset_size = find_largest_subset_size(
                index + 1, total_zeroes, total_ones
            )
            zeroes = strs[index].count("0")
            ones = len(strs[index]) - zeroes
            new_total_zeroes = total_zeroes + zeroes
            new_total_ones = total_ones + ones
            if new_total_zeroes <= m and new_total_ones <= n:
                largest_subset_size = max(
                    largest_subset_size,
                    1
                    + find_largest_subset_size(
                        index + 1, new_total_zeroes, new_total_ones
                    ),
                )
            return largest_subset_size

        return find_largest_subset_size(0, 0, 0)
