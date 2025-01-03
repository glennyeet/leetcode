class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # Prefix sum: O(n) time, O(n) space

        n = len(nums)
        prefix_sums = [0] * n
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_sums[i] = prefix_sum
        valid_splits = 0
        for i in range(n - 1):
            if prefix_sums[i] >= prefix_sum - prefix_sums[i]:
                valid_splits += 1
        return valid_splits
