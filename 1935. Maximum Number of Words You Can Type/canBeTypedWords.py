class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # String: O(n) time, O(n) space, where n is the size of text

        words = text.split()
        typable_words = len(words)
        for word in words:
            for letter in word:
                if letter in brokenLetters:
                    typable_words -= 1
                    break
        return typable_words
