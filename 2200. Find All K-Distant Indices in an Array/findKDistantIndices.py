from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # Two Pointers: O(n) time, O(n) space

        n = len(nums)
        k_distant_indices = []
        last_distant_index = -1
        for i, num in enumerate(nums):
            if num == key:
                for j in range(max(last_distant_index + 1, i - k), min(n, i + k + 1)):
                    k_distant_indices.append(j)
                last_distant_index = i + k
        return k_distant_indices
