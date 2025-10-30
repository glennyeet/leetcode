from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Greedy: O(n) time, O(1) space, where n is the size
        # of target

        min_operations = 0
        prev_num = 0
        for num in target:
            if num > prev_num:
                min_operations += num - prev_num
            prev_num = num
        return min_operations
