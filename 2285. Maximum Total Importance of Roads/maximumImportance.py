# import heapq


class MinHeap:
    nodes: list[int]

    def __init__(self, nodes: list[int] = []):
        self.nodes = []
        for node in nodes:
            self.insert(node)

    def __len__(self) -> int:
        return len(self.nodes)

    def __get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index: int) -> int:
        return child_index // 2 - 1

    def __has_left_child(self, parent_index: int) -> bool:
        return self.__get_left_child_index(parent_index) < self.__len__()

    def __has_right_child(self, parent_index: int) -> bool:
        return self.__get_right_child_index(parent_index) < self.__len__()

    def __has_parent(self, index: int) -> bool:
        return self.__get_parent_index(index) >= 0

    def __left_child(self, index: int) -> int:
        if not self.__has_left_child(index):
            return None
        return self.nodes[self.__get_left_child_index(index)]

    def __right_child(self, index: int) -> int:
        if not self.__has_right_child(index):
            return None
        return self.nodes[self.__get_right_child_index(index)]

    def __parent(self, index: int) -> int:
        if not self.__has_parent(index):
            return None
        return self.nodes[self.__get_parent_index(index)]

    def __swap(self, first_index: int, second_index: int):
        if first_index >= self.__len__() or second_index >= self.__len__():
            return
        self.nodes[first_index], self.nodes[second_index] = (
            self.nodes[second_index],
            self.nodes[first_index],
        )

    def __heapify_up(self, child_index: int = None) -> list[int]:
        if not child_index:
            child_index = self.__len__() - 1
        parent_index = self.__get_parent_index(child_index)
        if self.__parent(child_index) and self.nodes[child_index] < self.__parent(
            child_index
        ):
            self.__swap(child_index, parent_index)
            self.__heapify_up(parent_index)
        return self.nodes

    def insert(self, item: int):
        self.nodes.append(item)
        self.__heapify_up()

    def __heapify_down(self, index: int = 0) -> list[int]:
        if index >= self.__len__() or not self.__has_left_child(index):
            return self.nodes
        smaller_child_index = self.__get_left_child_index(index)
        if self.__has_right_child(index) and self.__right_child(
            index
        ) < self.__left_child(index):
            smaller_child_index = self.__get_right_child_index(index)
        if self.nodes[index] < self.nodes[smaller_child_index]:
            return self.nodes
        if self.nodes[index] > self.nodes[smaller_child_index]:
            self.__swap(index, smaller_child_index)
            return self.__heapify_down(smaller_child_index)

    def pop(self) -> int:
        if self.__len__() == 0:
            return None
        removed_node = self.nodes[0]
        self.nodes[0] = self.nodes[self.__len__() - 1]
        del self.nodes[-1]
        self.__heapify_down()
        return removed_node

    def peek(self) -> int:
        if self.__len() == 0:
            return None
        return self.nodes[0]

    def heap_sort(array: list[int]) -> list[int]:
        heap = MinHeap(array)
        sorted_array = []
        for _ in range(len(array)):
            sorted_array.append(heap.pop())
        return sorted_array

    def __heapify_children(self, index: int):
        if not self.__has_left_child(index) or self.__has_right_child(index):
            return
        if self.__right_child(index) < self.__left_child(index):
            self.__swap(
                self.__get_right_child_index(index), self.__get_left_child_index(index)
            )
        self.__heapify_children(self.__get_left_child_index(index))
        self.__heapify_children(self.__get_right_child_index(index))

    def heap_sort_in_place(array: list[int]) -> list[int]:
        heap = MinHeap(array)
        heap.nodes = array
        for i in range(len(array) // 2, -1, -1):
            heap.__heapify_down(i)


class Solution:
    def heapify(self, array: list[int], root: int):
        smallest = root
        l = 2 * root + 1
        r = 2 * root + 2
        if l < len(array) and array[l] < array[smallest]:
            smallest = l
        if r < len(array) and array[r] < array[smallest]:
            smallest = r
        if smallest != root:
            array[root], array[smallest] = array[smallest], array[root]
            self.heapify(array, smallest)

    def buildHeap(self, array: list[int]):
        start = len(array) // 2 - 1
        for i in range(start, -1, -1):
            self.heapify(array, i)

    def getLeftChildIndex(self, parentIndex: int) -> int:
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex: int) -> int:
        return 2 * parentIndex + 2

    def hasLeftChild(self, heap: list[int], parentIndex: int) -> bool:
        return self.getLeftChildIndex(parentIndex) < len(heap)

    def hasRightChild(self, heap: list[int], parentIndex: int) -> bool:
        return self.getRightChildIndex(parentIndex) < len(heap)

    def leftChild(self, heap: list[int], index: int) -> int:
        if not self.hasLeftChild(heap, index):
            return None
        return heap[self.getLeftChildIndex(index)]

    def rightChild(self, heap: list[int], index: int) -> int:
        if not self.hasRightChild(heap, index):
            return None
        return heap[self.getRightChildIndex(index)]

    def swap(self, heap: list[int], firstIndex: int, secondIndex: int):
        if firstIndex >= len(heap) or secondIndex >= len(heap):
            return
        heap[firstIndex], heap[secondIndex] = (
            heap[secondIndex],
            heap[firstIndex],
        )

    def heapifyDown(self, heap: list[int], index: int = 0) -> list[int]:
        if index >= len(heap) or not self.hasLeftChild(heap, index):
            return heap
        smaller_child_index = self.getLeftChildIndex(index)
        if self.hasRightChild(heap, index) and self.rightChild(
            heap, index
        ) < self.leftChild(heap, index):
            smaller_child_index = self.getRightChildIndex(index)
        if heap[index] < heap[smaller_child_index]:
            return heap
        if heap[index] > heap[smaller_child_index]:
            self.swap(heap, index, smaller_child_index)
            return self.heapifyDown(heap, smaller_child_index)

    def pop(self, heap: list[int]) -> int:
        if len(heap) == 0:
            return None
        removed_node = heap[0]
        heap[0] = heap[len(heap) - 1]
        del heap[-1]
        self.heapifyDown(heap)
        return removed_node

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        counter = [0] * n
        for i in range(len(roads)):
            counter[roads[i][0]] -= 1
            counter[roads[i][1]] -= 1
        # heapq.heapify(counter)
        self.buildHeap(counter)
        importance = n
        total = 0
        while counter:
            # total += importance * -heapq.heappop(counter)
            total += importance * -self.pop(counter)
            importance -= 1
        return total
