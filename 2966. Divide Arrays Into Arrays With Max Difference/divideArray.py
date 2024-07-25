class Solution:
    def mergeSort(self, array: list[int]):
        if len(array) > 1:
            m = len(array) // 2
            L = array[m:]
            R = array[:m]
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

    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        result = []
        self.mergeSort(nums)
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            else:
                result.append([nums[i], nums[i + 1], nums[i + 2]])
        return result
