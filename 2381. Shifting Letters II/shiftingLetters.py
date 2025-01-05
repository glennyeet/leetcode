class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Prefix sum: O(n) time, O(n) space

        n = len(s)
        prefix_diffs = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction == 1:
                prefix_diffs[start] += -1
                prefix_diffs[end + 1] += 1
            else:
                prefix_diffs[start] += 1
                prefix_diffs[end + 1] += -1
        shift = 0
        s_list = []
        for char in s:
            s_list.append(ord(char) - ord("a"))
        for i in reversed(range(n)):
            shift += prefix_diffs[i + 1]
            s_list[i] = chr((s_list[i] + shift) % 26 + ord("a"))
        return "".join(s_list)
