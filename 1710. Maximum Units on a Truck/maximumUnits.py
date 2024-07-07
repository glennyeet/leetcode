class Solution:
    def mergesort(self, array):
        if len(array) > 1:
            m = len(array) // 2
            L = array[:m]
            R = array[m:]
            self.mergesort(L)
            self.mergesort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i][1] >= R[j][1]:
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

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # boxTypes = sorted(boxTypes, key=lambda l: l[1], reverse=True)
        self.mergesort(boxTypes)
        maxUnits = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            numberOfBoxes = boxTypes[i][0]
            numberOfUnitsPerBox = boxTypes[i][1]
            boxesTaken = min(numberOfBoxes, truckSize)
            maxUnits += boxesTaken * numberOfUnitsPerBox
            truckSize -= boxesTaken
            i += 1
        return maxUnits
