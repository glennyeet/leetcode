from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Math: O(n) time, O(n) space

        nums_left = n
        addends = []
        if nums_left % 2:
            addends.append(0)
            nums_left -= 1
        num = 1
        while nums_left:
            addends.extend([num, -num])
            nums_left -= 2
            num += 1
        return addends
