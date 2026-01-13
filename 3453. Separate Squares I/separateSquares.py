from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Binary Search: O(n * log(n)) time, O(1) space, where n
        # is the size of squares

        total_area = 0
        for _, _, l in squares:
            total_area += l**2
        left = 0.0
        right = 1e9

        def is_gte_half(target_y: float) -> bool:
            area = 0.0
            for _, y, l in squares:
                if y <= target_y <= y + l:
                    area += (target_y - y) * l
                elif y + l <= target_y:
                    area += l**2
                if area * 2.0 >= total_area:
                    return True
            return area * 2.0 >= total_area

        for _ in range(50):
            mid = (left + right) / 2
            if is_gte_half(mid):
                right = mid
            else:
                left = mid
        return left
