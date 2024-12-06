class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        allowed_nums = []
        for i in range(1, n + 1):
            if i not in banned_set:
                allowed_nums.append(i)
        nums_sum = sum(allowed_nums)
        r = len(allowed_nums) - 1
        while r >= 0 and nums_sum > maxSum:
            nums_sum -= allowed_nums[r]
            r -= 1
        return r + 1
