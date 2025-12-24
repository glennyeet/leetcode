from typing import List


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Greedy: O(n * log(n)) time, O(n) space, where n is the size of
        # capacity

        total_apples = sum(apple)
        total_capacity = 0
        min_boxes = 0
        for apples in sorted(capacity, reverse=True):
            total_capacity += apples
            min_boxes += 1
            if total_capacity >= total_apples:
                break
        return min_boxes
