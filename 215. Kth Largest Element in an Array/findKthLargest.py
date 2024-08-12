import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_heap = []
        for num in nums:
            heapq.heappush(nums_heap, num)
            if len(nums_heap) > k:
                heapq.heappop(nums_heap)
        kth_largest = nums_heap[0]
        return kth_largest
