from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Hash map: O(n) time, O(n) space, where n is the
        # size of nums

        unique_nums_gt_k = set()
        for num in nums:
            if num < k:
                return -1
            if num > k:
                unique_nums_gt_k.add(num)
        return len(unique_nums_gt_k)
