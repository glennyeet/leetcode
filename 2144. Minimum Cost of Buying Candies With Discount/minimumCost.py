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

    def minimumCost(self, cost: List[int]) -> int:
        self.mergeSort(cost)
        minCost = sum(cost)
        if len(cost) > 2:
            for i in range(2, len(cost) // 3 * 3, 3):
                minCost -= cost[i]
        return minCost
