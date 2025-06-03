from typing import List
from collections import deque


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        # BFS + Hash Table: O(n^2) time, O(n) space, where
        # n is the size of status (number of boxes)

        max_candies = 0
        queue = deque()
        unopened_boxes = set()
        for box in initialBoxes:
            if status[box]:
                queue.append(box)
            else:
                unopened_boxes.add(box)
        unused_keys = set()
        while queue:
            cur_box = queue.popleft()
            max_candies += candies[cur_box]
            for box in containedBoxes[cur_box]:
                if status[box]:
                    queue.append(box)
                else:
                    unopened_boxes.add(box)
            for key in keys[cur_box]:
                unused_keys.add(key)
            new_unopened_boxes = unopened_boxes.copy()
            for box in unopened_boxes:
                if box in unused_keys:
                    queue.append(box)
                    new_unopened_boxes.remove(box)
                    unused_keys.remove(box)
            unopened_boxes = new_unopened_boxes.copy()
        return max_candies
