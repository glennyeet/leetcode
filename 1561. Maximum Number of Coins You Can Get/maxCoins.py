class Solution:
    # def partition(self, array: List[int], low: int, high: int) -> int:
    #     pivot = array[high]
    #     i = low - 1
    #     for j in range(low, high):
    #         if array[j] <= pivot:
    #             i += 1
    #             array[i], array[j] = array[j], array[i]
    #     array[i + 1], array[high] = array[high], array[i + 1]
    #     return i + 1

    # def quickSort(self, array: List[int], low: int, high: int):
    #     if low < high:
    #         pi = self.partition(array, low, high)
    #         self.quickSort(array, 0, pi - 1)
    #         self.quickSort(array, pi + 1, high)

    # def mergeSort(self, array: List[int]):
    #     if len(array) > 1:
    #         m = len(array) // 2
    #         L = array[:m]
    #         R = array[m:]
    #         self.mergeSort(L)
    #         self.mergeSort(R)
    #         i = j = k = 0
    #         while i < len(L) and j < len(R):
    #             if L[i] <= R[j]:
    #                 array[k] = L[i]
    #                 i += 1
    #             else:
    #                 array[k] = R[j]
    #                 j += 1
    #             k += 1
    #         while i < len(L):
    #             array[k] = L[i]
    #             i += 1
    #             k += 1
    #         while j < len(R):
    #             array[k] = R[j]
    #             j += 1
    #             k += 1

    def maxCoins(self, piles: List[int]) -> int:
        # self.quickSort(piles, 0, len(piles) - 1)
        # self.mergeSort(piles)
        piles.sort()
        coins = 0
        i = 0
        j = len(piles) - 1
        while i < j:
            coins += piles[j - 1]
            i += 1
            j -= 2
        return coins
