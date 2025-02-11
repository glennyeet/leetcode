class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Built-in functions: O(n^2 / m) time, O(n) space,
        # where n is the length of s

        # m = len(part)
        # result = s
        # while result.find(part) != -1:
        #     index = result.find(part)
        #     result = result[:index] + result[index + m :]
        # return result

        # Stack: O(n * m) time, O(n) space, where
        # n is the length of s

        # m = len(part)
        # s_stack = []
        # for char in s:
        #     s_stack.append(char)
        #     if len(s_stack) >= m:
        #         s_suffix = "".join(s_stack[-m:])
        #         if s_suffix == part:
        #             for _ in range(m):
        #                 s_stack.pop()
        # return "".join(s_stack)

        # Knuth-Morris-Pratt: O(m + n) time, O(m + n) space

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

        m = len(part)
        n = len(s)
        s_stack = []
        lps_table = get_lps_table(part)
        s_index = 0
        part_index = 0
        part_start_indices = [0] * (n + 1)
        while s_index < n:
            if part[part_index] == s[s_index]:
                s_stack.append(s[s_index])
                s_index += 1
                part_index += 1
                part_start_indices[len(s_stack)] = part_index
            elif part_index == 0:
                s_stack.append(s[s_index])
                s_index += 1
                part_start_indices[len(s_stack)] = 0
            else:
                part_index = lps_table[part_index - 1]
            if part_index == m:
                for _ in range(m):
                    s_stack.pop()
                part_index = part_start_indices[len(s_stack)]
        return "".join(s_stack)
