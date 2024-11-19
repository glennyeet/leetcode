from collections import Counter


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counter = Counter()
        l = 0
        r = 0
        max_sum = 0
        cur_sum = 0
        while l < n and r < n:
            while r < n and r - l < k and counter[nums[r]] == 0:
                counter[nums[r]] += 1
                cur_sum += nums[r]
                r += 1
            if r - l == k:
                max_sum = max(max_sum, cur_sum)
            cur_sum -= nums[l]
            counter[nums[l]] -= 1
            l += 1
            while l < r and counter[nums[l]] > 1:
                cur_sum -= nums[l]
                counter[nums[l]] -= 1
                l += 1
        return max_sum
