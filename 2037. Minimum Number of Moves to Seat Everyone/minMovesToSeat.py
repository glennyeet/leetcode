class Solution:
    # def partition(self, array, low, high):
    #     pivot = array[high]
    #     i = low - 1
    #     for j in range(low, high):
    #         if array[j] <= pivot:
    #             i += 1
    #             (array[i], array[j]) = (array[j], array[i])
    #     (array[i + 1], array[high]) = (array[high], array[i + 1])
    #     return i + 1

    # def quicksort(self, array, low, high):
    #     if low < high:
    #         pi = self.partition(array, low, high)
    #         self.quicksort(array, low, pi - 1)
    #         self.quicksort(array, pi + 1, high)

    def mergesort(self, array):
        if len(array) > 1:
            m = len(array) // 2
            L = array[:m]
            R = array[m:]
            self.mergesort(L)
            self.mergesort(R)
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

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # seats.sort()
        # students.sort()
        # self.quicksort(seats, 0, len(seats) - 1)
        # self.quicksort(students, 0, len(students) - 1)
        self.mergesort(seats)
        self.mergesort(students)
        min_moves = 0
        for i in range(len(seats)):
            min_moves += abs(seats[i] - students[i])
        return min_moves
