class Solution:
    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quickSort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        i = 0
        zeroExists = False
        self.quickSort(nums, 0, len(nums) - 1)
        while i < len(nums) and k != 0:
            if nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
            elif nums[i] == 0:
                zeroExists = True
            i += 1
        if not zeroExists and k != 0:
            self.quickSort(nums, 0, len(nums) - 1)
            i = 0
            while i < len(nums) and k != 0:
                if nums[i] != 0:
                    nums[i] = -nums[i]
                    k -= 1
                else:
                    i += 1
        return sum(nums)
