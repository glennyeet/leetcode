from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # Math: O(log(k)) time, O(1) space

        shift = 0
        for i, operation in enumerate(operations):
            if 1 << i & k - 1 and operation == 1:
                shift = (shift + 1) % 26
        return chr(ord("a") + shift)
