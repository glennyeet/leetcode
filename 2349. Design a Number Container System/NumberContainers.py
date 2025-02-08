from collections import defaultdict
from heapq import heappush, heappop


class NumberContainers:
    # Let n be the number of indices storing numbers

    def __init__(self):
        self.index_to_number = {}
        self.number_to_index = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        # Hash table + Heap: O(log(n)) time, O(n) space

        self.index_to_number[index] = number
        heappush(self.number_to_index[number], index)

    def find(self, number: int) -> int:
        # Hash table + Heap: O(klog(n)) time, O(n) space,
        # where k is the number of discarded indices in the heap

        if not self.number_to_index[number]:
            return -1
        while self.number_to_index[number]:
            index = self.number_to_index[number][0]
            if self.index_to_number[index] == number:
                return index
            heappop(self.number_to_index[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
