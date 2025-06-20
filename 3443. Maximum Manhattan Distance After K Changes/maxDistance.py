from collections import Counter


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        # Hash Table: O(n) time, O(1) space, where
        # n is the size of s

        directions_counter = Counter()
        max_manhattan_distance = 0
        for direction in s:
            directions_counter[direction] += 1
            max_x = max(directions_counter["W"], directions_counter["E"])
            min_x = min(directions_counter["W"], directions_counter["E"])
            remaining_changes = k
            x_changes = min(min_x, remaining_changes)
            min_x -= x_changes
            remaining_changes -= x_changes
            max_x += x_changes
            max_y = max(directions_counter["N"], directions_counter["S"])
            min_y = min(directions_counter["N"], directions_counter["S"])
            y_changes = min(min_y, remaining_changes)
            min_y -= y_changes
            max_y += y_changes
            max_manhattan_distance = max(
                max_manhattan_distance, max_x - min_x + max_y - min_y
            )
        return max_manhattan_distance
