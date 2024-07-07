class Solution:
    def mergeSort(self, array):
        if len(array) > 1:
            m = len(array) // 2
            L = array[:m]
            R = array[m:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1

    # def minimumOperations(self, nums: List[int]) -> int:
    #     self.mergeSort(nums)
    #     minOperations = 0
    #     i = 0
    #     while i < len(nums):
    #         num = nums[i]
    #         if num > 0:
    #             for j in range(len(nums)):
    #                 if nums[j] > 0:
    #                     nums[j] -= num
    #             minOperations += 1
    #         i += 1
    #     return minOperations
    # def minimumOperations(self, nums: List[int]) -> int:
    #     nums = set([num for num in nums if num != 0])
    #     return len(nums)
    def minimumOperations(self, nums: List[int]) -> int:
        self.mergeSort(nums)
        minOperations = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if (i == 0) or (i > 0 and nums[i] != nums[i - 1]):
                    minOperations += 1
        return minOperations
