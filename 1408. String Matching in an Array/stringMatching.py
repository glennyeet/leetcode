class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Knuth-Morris-Pratt: O(m * n^2) time, O(n * m) space, where n is the number of words,
        # m is the length of the longest word

        def get_lps_table(substring: str) -> list[int]:
            m = len(substring)
            lps_table = [0] * m
            i = 1
            prev_lps = 0
            while i < m:
                if substring[prev_lps] == substring[i]:
                    prev_lps += 1
                    lps_table[i] = prev_lps
                    i += 1
                elif prev_lps == 0:
                    i += 1
                else:
                    prev_lps = lps_table[prev_lps - 1]
            return lps_table

        def is_substring(substring: str, string: str, lps_table: list[int]) -> bool:
            m = len(substring)
            n = len(string)
            substring_index = 0
            string_index = 0
            while string_index < n:
                if string[string_index] == substring[substring_index]:
                    substring_index += 1
                    string_index += 1
                elif substring_index == 0:
                    string_index += 1
                else:
                    substring_index = lps_table[substring_index - 1]
                if substring_index == m:
                    return True
            return False

        valid_substrings = []
        for possible_substring in words:
            for word in words:
                if possible_substring == word:
                    continue
                if is_substring(
                    possible_substring, word, get_lps_table(possible_substring)
                ):
                    valid_substrings.append(possible_substring)
                    break
        return valid_substrings
