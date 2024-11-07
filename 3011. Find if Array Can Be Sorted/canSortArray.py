from math import inf


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # O(n^2) runtime, O(1) space

        # def bubble_sort(array: list[int]) -> bool:
        #     for i in range(len(array)):
        #         swapped = False
        #         for j in range(len(array) - i - 1):
        #             if array[j] > array[j + 1]:
        #                 if array[j].bit_count() != array[j + 1].bit_count():
        #                     return False
        #                 array[j], array[j + 1] = array[j + 1], array[j]
        #                 swapped = True
        #         if not swapped:
        #             break
        #     return True

        # return bubble_sort(nums.copy())

        # O(n) runtime, O(1) space
        cur_min = nums[0]
        cur_max = nums[0]
        prev_max = -inf
        for num in nums:
            if num.bit_count() == cur_min.bit_count():
                cur_min = min(cur_min, num)
                cur_max = max(cur_max, num)
            else:
                if prev_max > cur_min:
                    return False
                prev_max = cur_max
                cur_min = num
                cur_max = num
        if prev_max > cur_min:
            return False
        return True
