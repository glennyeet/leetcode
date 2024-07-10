class Solution:
    def minimumPushes(self, word: str) -> int:
        wordLen = len(word)
        pushes = 0
        cost = 1
        while wordLen > 0:
            pushes += min(8, wordLen) * cost
            wordLen -= 8
            cost += 1
        return pushes
