class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # Counting: O(n + m) time, O(1) space, where n is the
        # size of s and n is the size of target

        target_letter_counter = [0] * 26
        for char in target:
            target_letter_counter[ord(char) - ord("a")] += 1
        s_letter_counter = [0] * 26
        for char in s:
            s_letter_counter[ord(char) - ord("a")] += 1
        max_copies = float("inf")
        for i, count in enumerate(target_letter_counter):
            if count == 0:
                continue
            max_copies = min(max_copies, s_letter_counter[i] // count)
        return max_copies
