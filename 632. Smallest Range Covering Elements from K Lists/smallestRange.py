from heapq import heappush, heappop


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pointers = []
        left = nums[0][0]
        right = nums[0][0]
        for i, array in enumerate(nums):
            left = min(left, array[0])
            right = max(right, array[0])
            heappush(pointers, (array[0], i, 0))
        min_range = [left, right]
        while True:
            _, array, index = heappop(pointers)
            index += 1
            if index >= len(nums[array]):
                return min_range
            new_pointer_num = nums[array][index]
            heappush(pointers, (new_pointer_num, array, index))
            left = pointers[0][0]
            right = max(right, new_pointer_num)
            new_range = right - left
            cur_min_range = min_range[1] - min_range[0]
            if (
                new_range < cur_min_range
                or new_range == cur_min_range
                and left < min_range[0]
            ):
                min_range = [left, right]
