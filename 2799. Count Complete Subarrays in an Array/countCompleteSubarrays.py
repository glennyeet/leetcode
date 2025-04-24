from typing import List
from collections import Counter


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # Brute Force: O(n^2) time, O(n) space

        # n = len(nums)
        # total_unique_nums = len(set(nums))
        # complete_subarrays = 0
        # for i in range(n):
        #     nums_counter = Counter()
        #     unique_nums = set()
        #     for j in range(i, n):
        #         nums_counter[nums[j]] += 1
        #         unique_nums.add(nums[j])
        #         if len(unique_nums) == total_unique_nums:
        #             complete_subarrays += 1
        # return complete_subarrays

        # Sliding Window: O(n) time, O(n) space

        n = len(nums)
        total_unique_nums = len(set(nums))
        complete_subarrays = 0
        i = 0
        nums_counter = Counter()
        unique_nums = set()
        for j in range(n):
            nums_counter[nums[j]] += 1
            unique_nums.add(nums[j])
            while len(unique_nums) == total_unique_nums:
                nums_counter[nums[i]] -= 1
                if not nums_counter[nums[i]]:
                    unique_nums.remove(nums[i])
                i += 1
            complete_subarrays += i
        return complete_subarrays
