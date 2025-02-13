from heapq import heapify, heappop, heappush


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Priority Queue: O(nlog(n)) time, O(n) space, where
        # n is the size of nums

        less_than_k_nums = []
        greater_than_equal_k_nums = []
        for num in nums:
            if num < k:
                less_than_k_nums.append(num)
            else:
                greater_than_equal_k_nums.append(num)
        heapify(less_than_k_nums)
        heapify(greater_than_equal_k_nums)
        operations = 0
        while less_than_k_nums:
            operations += 1
            x = heappop(less_than_k_nums)
            if less_than_k_nums:
                y = heappop(less_than_k_nums)
            else:
                y = heappop(greater_than_equal_k_nums)
            new_num = min(x, y) * 2 + max(x, y)
            if new_num < k:
                heappush(less_than_k_nums, new_num)
            else:
                heappush(greater_than_equal_k_nums, new_num)
        return operations
