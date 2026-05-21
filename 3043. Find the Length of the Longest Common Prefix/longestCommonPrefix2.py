from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Hash Table + Math: O((m + n) * log(m + n)) time, O(m + n) space

        def get_prefixes(nums: list[int]) -> set[int]:
            prefixes = set()
            for num in nums:
                while num != 0:
                    prefixes.add(num)
                    num //= 10
            return prefixes

        arr1_prefixes = get_prefixes(arr1)
        arr2_prefixes = get_prefixes(arr2)
        common_prefixes = arr1_prefixes & arr2_prefixes
        if not common_prefixes:
            return 0
        longest_prefix = max(common_prefixes)
        prefix_length = 0
        while longest_prefix != 0:
            prefix_length += 1
            longest_prefix //= 10
        return prefix_length
