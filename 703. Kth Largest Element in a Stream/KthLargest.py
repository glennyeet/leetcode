import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums_heap = []
        for num in nums:
            heapq.heappush(self.nums_heap, num)
            if len(self.nums_heap) > k:
                heapq.heappop(self.nums_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums_heap, val)
        if len(self.nums_heap) > self.k:
            heapq.heappop(self.nums_heap)
        kth_largest = self.nums_heap[0]
        return kth_largest


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
