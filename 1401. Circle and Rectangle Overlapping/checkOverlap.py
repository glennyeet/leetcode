from math import sqrt


class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # Geometry: O(n * m) time, O(1) space, where n is x2 - x1
        # and m is y2 - y1

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                d = sqrt((x - xCenter) ** 2 + (y - yCenter) ** 2)
                if d <= float(radius):
                    return True
        return False
