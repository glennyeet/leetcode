from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if not p:
            return 0
        n = len(nums)
        sorted_nums = sorted(nums)
        left = 0
        right = 10**9

        def is_valid_difference(difference: int) -> bool:
            used_indices = [False] * n
            pairs = 0
            for i in range(n - 1):
                if used_indices[i]:
                    continue
                if sorted_nums[i + 1] - sorted_nums[i] <= difference:
                    used_indices[i + 1] = True
                    used_indices[i] = True
                    pairs += 1
                if pairs >= p:
                    return True
            return pairs >= p

        while left < right:
            mid = (left + right) // 2
            if is_valid_difference(mid):
                right = mid
            else:
                left = mid + 1
        return left
