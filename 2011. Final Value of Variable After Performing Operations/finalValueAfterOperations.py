from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        final_value = 0
        for operation in operations:
            if operation == "++X" or operation == "X++":
                final_value += 1
            else:
                final_value -= 1
        return final_value
