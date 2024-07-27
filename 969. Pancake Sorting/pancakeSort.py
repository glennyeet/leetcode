class Solution:
    def swap(self, array: list[int], end: int):
        i = 0
        j = end
        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    def findMaxIndex(self, array: list[int], end: int) -> int:
        i = index = 0
        while i <= end:
            if array[i] > array[index]:
                index = i
            i += 1
        return index

    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                break
            if i == len(arr):
                return flips
        sortedArray = arr
        for i in range(len(sortedArray) - 1, -1, -1):
            maxIndex = self.findMaxIndex(sortedArray, i)
            if maxIndex != i:
                if maxIndex != 0:
                    self.swap(sortedArray, maxIndex)
                    flips.append(maxIndex + 1)
                self.swap(sortedArray, i)
                flips.append(i + 1)
        return flips
