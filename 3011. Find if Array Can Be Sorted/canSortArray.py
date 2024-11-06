class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def bubble_sort(array: list[int]) -> bool:
            for i in range(len(array)):
                swapped = False
                for j in range(len(array) - i - 1):
                    if array[j] > array[j + 1]:
                        if array[j].bit_count() != array[j + 1].bit_count():
                            return False
                        array[j], array[j + 1] = array[j + 1], array[j]
                        swapped = True
                if not swapped:
                    break
            return True

        return bubble_sort(nums.copy())
