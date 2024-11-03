from bisect import bisect_left
from math import inf


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom-up Dynamic Programming with O(n^2) runtime

        # n = len(nums)
        # lengths = [1] * n
        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             lengths[i] = max(lengths[i], 1 + lengths[j])
        # return max(lengths)

        # Binary Search with O(nlog(n)) runtime
        # def binary_search(num: int, nums_list: list[int]) -> int:
        #     low = 0
        #     high = len(nums_list)
        #     while low < high:
        #         mid = low + (high - low) // 2
        #         if nums_list[mid] < num:
        #             low = mid + 1
        #         else:
        #             high = mid
        #     return low

        lengths = []
        smallest_nums = [-inf]
        for num in nums:
            # index = binary_search(num, smallest_nums)
            index = bisect_left(smallest_nums, num)
            if index == len(smallest_nums):
                smallest_nums.append(num)
            else:
                smallest_nums[index] = num
            lengths.append(index)
        return max(lengths)
