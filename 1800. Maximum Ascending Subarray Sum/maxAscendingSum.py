class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # One-pass: O(n) time, O(1) space

        n = len(nums)
        max_sum = nums[0]
        cur_sum = nums[0]
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                cur_sum += nums[i]
                max_sum = max(max_sum, cur_sum)
            else:
                cur_sum = nums[i]
        return max_sum
