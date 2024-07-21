class Solution:
    def minFlips(self, target: str) -> int:
        operations = 0
        if target[0] == "1":
            operations += 1
        for i in range(1, len(target)):
            if target[i] != target[i - 1]:
                operations += 1
        return operations
