from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # BFS: O(n) time, O(n) space

        n = len(s)
        strings_queue = deque([s])
        unique_strings = set([s])
        min_string = s
        rotation_start_index = n - b % n
        while strings_queue:
            string = strings_queue.popleft()
            min_string = min(min_string, string)
            added_string = list(string)
            for i, char in enumerate(added_string):
                if i % 2 == 1:
                    added_string[i] = str((int(char) + a) % 10)
            added_string = "".join(added_string)
            if added_string not in unique_strings:
                strings_queue.append(added_string)
                unique_strings.add(added_string)
            rotated_string = (
                string[rotation_start_index:] + string[:rotation_start_index]
            )
            if rotated_string not in unique_strings:
                strings_queue.append(rotated_string)
                unique_strings.add(rotated_string)
        return min_string
