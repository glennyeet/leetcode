class Solution:
    def parition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quickSort(self, array, low, high):
        if low < high:
            pi = self.parition(array, low, high)
            self.quickSort(array, low, pi - 1)
            self.quickSort(array, pi + 1, high)

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        contentChildren = 0
        i = j = 0
        self.quickSort(g, 0, len(g) - 1)
        self.quickSort(s, 0, len(s) - 1)
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                contentChildren += 1
                i += 1
                j += 1
            else:
                j += 1
        return contentChildren
