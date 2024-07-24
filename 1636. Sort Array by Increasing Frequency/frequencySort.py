class Solution:
    def mergeSort(self, array: list[int], counter: dict[int, int]):
        if len(array) > 1:
            m = len(array) // 2
            L = array[:m]
            R = array[m:]
            self.mergeSort(L, counter)
            self.mergeSort(R, counter)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if (
                    counter.get(L[i]) < counter.get(R[j])
                    or counter.get(L[i]) == counter.get(R[j])
                    and L[i] >= R[j]
                ):
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

    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        sortedNums = nums
        self.mergeSort(sortedNums, counter)
        return sortedNums
