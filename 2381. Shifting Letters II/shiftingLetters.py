class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # Prefix sum: O(n) time, O(n) space

        n = len(s)
        prefix_diffs = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction == 1:
                prefix_diffs[start] += 1
                prefix_diffs[end + 1] += -1
            else:
                prefix_diffs[start] += -1
                prefix_diffs[end + 1] += 1
        shift = 0
        s_list = []
        for char in s:
            s_list.append(ord(char) - ord("a"))
        for i, num in enumerate(s_list):
            shift += prefix_diffs[i]
            s_list[i] = chr((num + shift) % 26 + ord("a"))
        return "".join(s_list)
