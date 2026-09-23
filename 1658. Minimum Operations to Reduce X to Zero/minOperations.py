class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # Sliding Window: O(n) time, O(1) space

        n = len(nums)
        target_subarray_sum = sum(nums) - x
        if target_subarray_sum < 0:
            return -1
        elif target_subarray_sum == 0:
            return n
        max_subarray_len = -1
        cur_subarray_sum = 0
        l = 0
        for r, num in enumerate(nums):
            cur_subarray_sum += num
            while cur_subarray_sum > target_subarray_sum and l <= r:
                cur_subarray_sum -= nums[l]
                l += 1
            if cur_subarray_sum == target_subarray_sum:
                max_subarray_len = max(max_subarray_len, r - l + 1)
        if max_subarray_len == -1:
            return -1
        return n - max_subarray_len
