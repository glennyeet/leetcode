from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Brute force: O(n) time, O(n) space, where n is the size
        # of nums

        lt_pivot = []
        eq_pivot = []
        gt_pivot = []
        for num in nums:
            if num < pivot:
                lt_pivot.append(num)
            elif num == pivot:
                eq_pivot.append(num)
            else:
                gt_pivot.append(num)
        return lt_pivot + eq_pivot + gt_pivot
