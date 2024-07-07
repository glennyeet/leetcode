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
                if L[i] >= R[j]:
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

    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        mid = total // 2
        self.mergeSort(nums)
        i = 0
        minSubsequence = []
        minSum = 0
        while minSum <= mid and i < len(nums):
            minSubsequence.append(nums[i])
            minSum += nums[i]
            i += 1
        return minSubsequence
