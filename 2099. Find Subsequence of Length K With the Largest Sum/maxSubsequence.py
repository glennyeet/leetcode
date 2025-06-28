from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Sorting: O(nlog(n)) time, O(n) space

        n = len(nums)
        nums_mappings = []
        for i, num in enumerate(nums):
            nums_mappings.append((num, i))
        nums_mappings.sort()
        max_subsequence_mappings = sorted(nums_mappings[n - k :], key=lambda x: x[1])
        max_subsequence = []
        for num, _ in max_subsequence_mappings:
            max_subsequence.append(num)
        return max_subsequence
