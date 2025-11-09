class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # Simulation: O(max(n, m)) time, O(1) space, where
        # n is num1 and m is num2

        operations = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            operations += 1
        return operations
