from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Greedy: O(n) time, O(n) space

        n = len(arr)
        sorted_arr = sorted(arr)
        max_element = 1
        for i in range(1, n):
            if sorted_arr[i] >= max_element + 1:
                max_element += 1
        return max_element
