class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        def count_subsets(or_sum: int, i: int):
            if i == len(nums):
                if or_sum == max_or:
                    return 1
                return 0
            return count_subsets(or_sum | nums[i], i + 1) + count_subsets(or_sum, i + 1)

        return count_subsets(0, 0)
