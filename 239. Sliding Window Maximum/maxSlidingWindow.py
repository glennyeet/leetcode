from typing import List
from heapq import heappush, heappop
from collections import Counter


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Priority Queue + Hash Table: O(n * log(n)) time, O(n) space

        n = len(nums)
        right = -1
        window_priority_queue = []
        window_counter = Counter()
        max_window_elements = []
        for left in range(n - k + 1):
            while right - left + 1 < k:
                right += 1
                heappush(window_priority_queue, -nums[right])
                window_counter[nums[right]] += 1
            while window_counter[-window_priority_queue[0]] == 0:
                heappop(window_priority_queue)
            max_window_elements.append(-window_priority_queue[0])
            window_counter[nums[left]] -= 1
        return max_window_elements
