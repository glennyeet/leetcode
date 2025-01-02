class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Prefix sum: O(n + q) time, O(n + q) space

        n = len(words)
        q = len(queries)
        vowels = ["a", "e", "i", "o", "u"]
        total_vowel_words = 0
        vowel_words = [0] * n
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                total_vowel_words += 1
            vowel_words[i] = total_vowel_words
        ans = [0] * q
        for i, [l, r] in enumerate(queries):
            ans[i] = vowel_words[r] - vowel_words[l]
            if words[l][0] in vowels and words[l][-1] in vowels:
                ans[i] += 1
        return ans
