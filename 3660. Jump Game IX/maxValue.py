from typing import List
from collections import defaultdict


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # Prefix Sum: O(n) time, O(n) space

        n = len(nums)
        ans = [0] * n
        prefix_max = [0] * n
        suffix_min = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        suffix_min[-1] = nums[-1]
        for i in reversed(range(n - 1)):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        ans[-1] = prefix_max[-1]
        for i in reversed(range(n - 1)):
            if prefix_max[i] > suffix_min[i + 1]:
                ans[i] = ans[i + 1]
            else:
                ans[i] = prefix_max[i]
        return ans
