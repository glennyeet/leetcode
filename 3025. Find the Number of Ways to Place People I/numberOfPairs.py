from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Enumeration: O(n^3) time, O(1) space, where n is the
        # size of points

        valid_pairs = 0
        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y1) == (x2, y2):
                    continue
                elif not (x1 <= x2 and y1 >= y2):
                    continue
                point_between = False
                for x3, y3 in points:
                    if (x3, y3) == (x1, y1) or (x3, y3) == (x2, y2):
                        continue
                    elif x1 <= x3 <= x2 and y2 <= y3 <= y1:
                        point_between = True
                        break
                valid_pairs += not point_between
        return valid_pairs
