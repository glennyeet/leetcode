class Solution:
    def mergeSort(self, array: list[int]):
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

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        i = j = tempSum = 0
        totalSums = n * (n + 1) / 2
        while j < len(nums) and len(sums) <= totalSums:
            tempSum += nums[j]
            sums.append(tempSum)
            j += 1
            if j >= len(nums):
                i += 1
                j = i
                tempSum = 0
        # self.mergeSort(sums)
        sums.sort()
        indexedSum = 0
        for k in range(left - 1, right):
            indexedSum += sums[k]
        indexedSum %= 10**9 + 7
        return indexedSum
