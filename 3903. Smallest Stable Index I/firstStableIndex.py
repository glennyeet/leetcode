class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # Prefix Sum: O(n) time, O(n) space, where n is the size of
        # nums

        max_num = [nums[0]]
        for num in nums:
            max_num.append(max(max_num[-1], num))
        reversed_min_num = [nums[-1]]
        for num in reversed(nums):
            reversed_min_num.append(min(reversed_min_num[-1], num))
        reversed_min_num.reverse()
        for i, num in enumerate(nums):
            if max_num[i] - reversed_min_num[i] <= k:
                return i
        return -1
