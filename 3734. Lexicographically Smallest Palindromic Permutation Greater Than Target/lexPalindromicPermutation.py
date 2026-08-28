from collections import Counter


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        # Enumeration: O(n^2) time, O(n) space

        n = len(s)

        def can_be_palindrome(string: str) -> bool:
            char_counter = Counter(string)
            odd_counts = 0
            for _, count in char_counter.items():
                odd_counts += count % 2 == 1
            return odd_counts <= 1

        if not can_be_palindrome(s):
            return ""

        def is_strictly_greater_than_target(
            char_counter: Counter[str], string: str
        ) -> bool:
            largest_string = string[:]
            remaining_char_counts = dict(char_counter.items())
            i = 0
            while i < n and largest_string[i] is not None:
                i += 1
            for char, count in sorted(remaining_char_counts.items(), reverse=True):
                while count >= 2:
                    largest_string[i] = char
                    largest_string[n - i - 1] = char
                    i += 1
                    count -= 2
                if count >= 1:
                    largest_string[n // 2] = char
                    count -= 1
            return "".join(largest_string) > target

        char_counter = Counter(s)
        prefix_matching = True
        ans = [None] * n
        for i in range((n + 1) // 2):
            if prefix_matching:
                target_char = target[i]
                char_copies_needed = 1 if i * 2 + 1 == n else 2
                if i * 2 + 1 != n and char_counter[target_char] >= 2:
                    char_counter[target_char] -= 2
                    ans[i] = target_char
                    ans[n - i - 1] = target_char
                    if is_strictly_greater_than_target(char_counter, ans):
                        continue
                    ans[i] = None
                    ans[n - i - 1] = None
                    char_counter[target_char] += 2
                    target_char = chr(ord(target_char) + 1)
                elif i * 2 + 1 == n and char_counter[target_char] >= 1:
                    char_counter[target_char] -= 1
                    ans[i] = target_char
                    if is_strictly_greater_than_target(char_counter, ans):
                        continue
                    ans[i] = None
                    char_counter[target_char] += 1
                    target_char = chr(ord(target_char) + 1)
                while (
                    char_counter[target_char] < char_copies_needed
                    and target_char <= "z"
                ):
                    target_char = chr(ord(target_char) + 1)
                if target_char > "z":
                    return ""
                char_counter[target_char] -= char_copies_needed
                ans[i] = target_char
                ans[n - i - 1] = target_char
                prefix_matching = False
            else:
                left = i
                for char, count in sorted(char_counter.items()):
                    while count >= 2:
                        ans[left] = char
                        ans[n - left - 1] = char
                        left += 1
                        count -= 2
                    if count >= 1:
                        ans[n // 2] = char
                        count -= 1
                return "".join(ans)
        return "".join(ans)
