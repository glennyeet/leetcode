class Solution:
    def partition(self, array: List[int], low: int, high: int) -> int:
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quickSort(self, array: List[int], low: int, high: int):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)

    def minPairSum(self, nums: List[int]) -> int:
        # self.quickSort(nums, 0 , len(nums) - 1)
        nums.sort()
        pairSum = 0
        for i in range(len(nums) // 2):
            if nums[i] + nums[len(nums) - 1 - i] > pairSum:
                pairSum = nums[i] + nums[len(nums) - 1 - i]
        return pairSum
