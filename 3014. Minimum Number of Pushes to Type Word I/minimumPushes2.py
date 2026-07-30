class Solution:
    def minimumPushes(self, word: str) -> int:
        # Math: O(1) time, O(1) space

        n = len(word)
        pushes = 0
        for i in range(n):
            pushes += i // 8 + 1
        return pushes
