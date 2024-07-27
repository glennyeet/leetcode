class Solution:
    def mergeSort(self, array: list[str]):
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

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1Array = list(s1)
        s2Array = list(s2)
        self.mergeSort(s1Array)
        self.mergeSort(s2Array)
        # s1Array = sorted(s1)
        # s2Array = sorted(s2)
        s1Larger = True
        s1S2Tuple = list(zip(s1Array, s2Array))
        for c1, c2 in s1S2Tuple:
            if c1 < c2:
                s1Larger = False
                break
        if s1Larger:
            for c1, c2 in s1S2Tuple:
                if c1 < c2:
                    return False
        else:
            for c1, c2 in s1S2Tuple:
                if c1 > c2:
                    return False
        return True
