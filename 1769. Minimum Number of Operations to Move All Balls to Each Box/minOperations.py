class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Prefix sum: O(n) time, O(n) space

        n = len(boxes)
        operations = [0] * n
        moves = 0
        moves_increase = 0
        for i, box in enumerate(boxes):
            operations[i] = moves
            if box == "1":
                moves_increase += 1
            moves += moves_increase
        moves = 0
        moves_increase = 0
        for i, box in reversed(list(enumerate(boxes))):
            operations[i] += moves
            if box == "1":
                moves_increase += 1
            moves += moves_increase
        return operations
