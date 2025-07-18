from typing import List
from heapq import heapify, heapreplace


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # Priority Queue: O(nlog(n)) time, O(n) space

        n = len(nums)
        m = n // 3
        first_pq = []
        second_pq = []
        for i in range(m):
            first_pq.append(-nums[i])
            second_pq.append(nums[-i - 1])
        heapify(first_pq)
        heapify(second_pq)
        first_sum = -sum(first_pq)
        second_sum = sum(second_pq)
        min_diff = first_sum - second_sum
        first_sums = [first_sum]
        second_sums = [second_sum]
        for i in range(m):
            third_num_left = nums[m + i]
            first_max = -first_pq[0]
            if third_num_left < first_max:
                first_sum = first_sum - first_max + third_num_left
                heapreplace(first_pq, -third_num_left)
            first_sums.append(first_sum)
            third_num_right = nums[m + m - i - 1]
            second_min = second_pq[0]
            if third_num_right > second_min:
                second_sum = second_sum - second_min + third_num_right
                heapreplace(second_pq, third_num_right)
            second_sums.append(second_sum)
        second_sums.reverse()
        for first_sum, second_sum in zip(first_sums, second_sums):
            min_diff = min(min_diff, first_sum - second_sum)
        return min_diff
