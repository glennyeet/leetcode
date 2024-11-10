from heapq import heappush, heappop


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums_heap = []
        for i, num in enumerate(nums):
            heappush(nums_heap, (num, i))
        next_greatest_indices = {}

        while nums_heap:
            num, i = heappop(nums_heap)
            next_greatest_num_index = -1
            j = i + 1
            if j >= len(nums):
                j = 0
            while j != i:
                if nums[j] > num:
                    next_greatest_num_index = j
                    break
                if j in next_greatest_indices:
                    if next_greatest_indices[j] == -1:
                        break
                    j = next_greatest_indices[j]
                else:
                    j += 1
                if j == len(nums):
                    j = 0
            next_greatest_indices[i] = next_greatest_num_index
        ans = [0] * len(nums)
        for key in next_greatest_indices:
            if next_greatest_indices[key] == -1:
                ans[key] = -1
            else:
                ans[key] = nums[next_greatest_indices[key]]
        return ans
