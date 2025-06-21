class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # Hash Table: O(n) time, O(1) space

        n = len(word)
        char_counter = [0] * 26
        for char in word:
            char_counter[ord(char) - ord("a")] += 1
        min_deletions = n
        for i in range(26):
            deletions = 0
            min_char_count = char_counter[i]
            for j, count in enumerate(char_counter):
                if i == j:
                    continue
                elif min_char_count > count:
                    deletions += count
                elif min_char_count + k < count:
                    deletions += count - (min_char_count + k)
            min_deletions = min(min_deletions, deletions)
        return min_deletions
