class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        max_beauty = 0
        max_diff = k * 2
        diff = 0
        l = 0
        for r in range(len(sorted_nums)):
            diff = sorted_nums[r] - sorted_nums[l]
            while l < r and diff > max_diff:
                l += 1
                diff = sorted_nums[r] - sorted_nums[l]
            max_beauty = max(max_beauty, r - l + 1)
        return max_beauty
