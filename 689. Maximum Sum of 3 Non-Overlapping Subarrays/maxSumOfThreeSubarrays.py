class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Top-down DP: O(n) time, O(n) space

        k_sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] - nums[i - k] + nums[i])
        dp = {}

        def get_max_sum(count: int, i: int) -> int:
            if count == 3 or i > len(nums) - k:
                return 0
            elif (count, i) in dp:
                return dp[(count, i)]
            sum_include_num = k_sums[i] + get_max_sum(count + 1, i + k)
            sum_skip_num = get_max_sum(count, i + 1)
            dp[(count, i)] = max(sum_include_num, sum_skip_num)
            return dp[(count, i)]

        j = 0
        indices = []
        while len(indices) < 3 and j + k <= len(nums):
            sum_include_num = k_sums[j] + get_max_sum(len(indices) + 1, j + k)
            sum_skip_num = get_max_sum(len(indices), j + 1)
            if sum_include_num >= sum_skip_num:
                indices.append(j)
                j += k
            else:
                j += 1
        return indices
