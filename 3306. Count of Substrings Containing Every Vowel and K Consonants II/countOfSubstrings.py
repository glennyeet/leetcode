class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # Sliding window: O(n) time, O(1) space

        n = len(word)

        def count_at_least_consonant_substrings(c: int) -> int:
            vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
            consonants = 0
            substrings = 0
            l = 0

            def contains_all_vowels():
                for vowel in vowels:
                    if vowels[vowel] == 0:
                        return False
                return True

            for r in range(n):
                right_letter = word[r]
                if right_letter in vowels:
                    vowels[right_letter] += 1
                else:
                    consonants += 1
                while contains_all_vowels() and consonants >= c:
                    substrings += n - r
                    left_letter = word[l]
                    if left_letter in vowels:
                        vowels[left_letter] -= 1
                    else:
                        consonants -= 1
                    l += 1
            return substrings

        return count_at_least_consonant_substrings(
            k
        ) - count_at_least_consonant_substrings(k + 1)
