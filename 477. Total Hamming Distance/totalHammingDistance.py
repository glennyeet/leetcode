class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        dist_sum = 0
        n = len(nums)
        for i in range(max(nums).bit_length()):
            ones = 0
            for num in nums:
                ones += num >> i & 1
            dist_sum += ones * (n - ones)
        return dist_sum
