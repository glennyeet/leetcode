from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # String: O(n) time, O(n) space, where n
        # is the size of strs

        encoded_string = []
        for string in strs:
            encoded_string.append(str(len(string)))
            encoded_string.append("#")
            encoded_string.append(string)
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        # String: O(n) time, O(n) space, where n is
        # is the size of s

        n = len(s)
        strings_list = []
        i = 0
        while i < n:
            string_length = []
            while s[i] != "#":
                string_length.append(s[i])
                i += 1
            string_length = int("".join(string_length))
            i += 1
            end_index = i + string_length
            strings_list.append(s[i:end_index])
            i = end_index
        return strings_list
