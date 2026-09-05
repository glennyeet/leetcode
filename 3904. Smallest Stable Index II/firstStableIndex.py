class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # Prefix Sum: O(n) time, O(n) space

        n = len(nums)
        max_num = [nums[0]]
        reversed_min_num = [nums[-1]]
        for i in range(1, n):
            max_num.append(max(max_num[-1], nums[i]))
            reversed_min_num.append(min(reversed_min_num[-1], nums[n - i - 1]))
        reversed_min_num.reverse()
        for i in range(n):
            if max_num[i] - reversed_min_num[i] <= k:
                return i
        return -1
