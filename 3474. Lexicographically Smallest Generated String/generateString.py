class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        # Greedy: O(n * m) time, O(n + m) space

        n = len(str1)
        m = len(str2)
        t_string = [""] * (n + m - 1)
        for i, char1 in enumerate(str1):
            if char1 != "T":
                continue
            for j, char2 in enumerate(str2):
                k = i + j
                if t_string[k] != "" and t_string[k] != char2:
                    return ""
                t_string[k] = char2
        f_string = []
        for char in t_string:
            if char == "":
                f_string.append("a")
            else:
                f_string.append(char)
        for i, char1 in enumerate(str1):
            if char1 != "F":
                continue
            elif "".join(f_string[i : i + m]) != str2:
                continue
            for j in reversed(range(i, i + m)):
                if t_string[j] == "":
                    f_string[j] = "b"
                    break
            else:
                return ""
        return "".join(f_string)
