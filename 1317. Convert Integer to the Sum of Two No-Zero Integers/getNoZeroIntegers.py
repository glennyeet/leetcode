from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Enumeration: O(nlog(n)) time, O(1) space

        def has_zero(num: int) -> bool:
            while num != 0:
                if num % 10 == 0:
                    return True
                num //= 10
            return False

        a = 1
        b = n - 1
        while has_zero(a) or has_zero(b):
            a += 1
            b -= 1
        return [a, b]
