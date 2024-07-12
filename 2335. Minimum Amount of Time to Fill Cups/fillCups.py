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

    def fillCups(self, amount: List[int]) -> int:
        minSeconds = 0
        while amount[0] != 0 or amount[1] != 0 or amount[2] != 0:
            self.mergeSort(amount)
            amount[0] -= 1
            if amount[1] > 0:
                amount[1] -= 1
            minSeconds += 1
        return minSeconds
