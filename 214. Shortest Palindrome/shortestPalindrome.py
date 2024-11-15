class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # def kmp(substring: str, string: str) -> bool:
        #     if substring == "":
        #         return 0
        #     m = len(substring)
        #     lps = [0] * m
        #     prev_lps = 0
        #     i = 1
        #     while i < m:
        #         if substring[i] == substring[prev_lps]:
        #             lps[i] = prev_lps + 1
        #             prev_lps += 1
        #             i += 1
        #         elif prev_lps == 0:
        #             lps[i] = prev_lps
        #             i += 1
        #         else:
        #             prev_lps = lps[prev_lps - 1]
        #     substring_index = 0
        #     string_index = 0
        #     while string_index < len(string):
        #         if string[string_index] == substring[substring_index]:
        #             substring_index += 1
        #             string_index += 1
        #         elif substring_index == 0:
        #             string_index += 1
        #         else:
        #             substring_index = lps[substring_index - 1]
        #         if substring_index == m:
        #             return string_index - m
        #     return -1

        def get_lps_table(string: str) -> list[int]:
            n = len(string)
            lps = [0] * n
            prev_lps = 0
            i = 1
            while i < n:
                if string[i] == string[prev_lps]:
                    lps[i] = prev_lps + 1
                    prev_lps += 1
                    i += 1
                elif prev_lps == 0:
                    i += 1
                else:
                    prev_lps = lps[prev_lps - 1]
            return lps

        search_string = s + "-" + s[::-1]
        lps_table = get_lps_table(search_string)
        return s[: lps_table[-1] - 1 : -1] + s
