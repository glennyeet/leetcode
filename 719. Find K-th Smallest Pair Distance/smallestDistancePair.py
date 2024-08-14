import bisect

class Solution:
    def partition(self, array: list[int], low: int, high: int) -> int:
        p = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= p:
                i += 1
                array[i], array[j] = array[j], array[i]
        i += 1
        array[i], array[high] = array[high], array[i]
        return i

    def quick_sort(self, array: list[int], low: int, high: int):
        if low < high:
            pi = self.partition(array, low, high)
            self.quick_sort(array, low, pi - 1)
            self.quick_sort(array, pi + 1, high)

    def pairs_less_than_mid(self, nums: list[int], mid: int, k: int):
        n = len(nums)
        count = 0
        index_right = bisect.bisect_right(nums, mid - nums[0]) - 1
        for i in range(len(nums)):
            while index_right + 1 < n and nums[index_right + 1] - nums[i] <= mid:
                index_right += 1
            count += index_right - i
        count_less_than_mid = count < k
        return count_less_than_mid

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.quick_sort(nums, 0, n - 1)
        # nums.sort()
        left = 0
        right = nums[-1]
        while left < right:
            mid = (left + right) // 2
            if self.pairs_less_than_mid(nums, mid, k):
                left = mid + 1
            else:
                right = mid
        return left

