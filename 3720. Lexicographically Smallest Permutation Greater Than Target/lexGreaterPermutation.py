from collections import Counter


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        # Hash Table + Enumeration: O(n^2) time, O(n) space

        n = len(target)
        char_counter = Counter(s)
        prefix_matches = True
        smallest_permutation = []
        for i in range(n):
            if prefix_matches:
                target_char = target[i]
                if char_counter[target_char] > 0:
                    char_counter[target_char] -= 1
                    max_permutation = [target_char]
                    for char, count in sorted(char_counter.items(), reverse=True):
                        max_permutation.append(char * count)
                    if "".join(smallest_permutation + max_permutation) > target:
                        smallest_permutation.append(target_char)
                        continue
                    char_counter[target_char] += 1
                    target_char = chr(ord(target_char) + 1)
                while char_counter[target_char] == 0 and target_char <= "z":
                    target_char = chr(ord(target_char) + 1)
                if target_char > "z":
                    return ""
                char_counter[target_char] -= 1
                smallest_permutation.append(target_char)
                prefix_matches = False
            else:
                for char, count in sorted(char_counter.items()):
                    smallest_permutation.append(char * count)
                return "".join(smallest_permutation)
        return "".join(smallest_permutation)
