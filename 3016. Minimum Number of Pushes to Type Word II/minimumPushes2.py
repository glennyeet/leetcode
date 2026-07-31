from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # Greedy: O(n) time, O(1) space, where n
        # is the size of word

        most_common_chars = Counter(word).most_common()
        pushes = 0
        for i, (_, count) in enumerate(most_common_chars):
            pushes += (i // 8 + 1) * count
        return pushes
