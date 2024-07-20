class Solution:
    def mergeSort(self, array: List[int]):
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

    def partitionArray(self, nums: List[int], k: int) -> int:
        self.mergeSort(nums)
        subseqs = 0
        i = j = 0
        while j < len(nums):
            if nums[j] - nums[i] > k:
                subseqs += 1
                i = j
            if j == len(nums) - 1:
                subseqs += 1
            j += 1
        return subseqs
