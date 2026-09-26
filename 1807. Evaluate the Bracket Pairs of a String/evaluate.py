class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # Hash Table: O(n + k) time, O(n + k) space, where k is
        # the size of knowledge

        n = len(s)
        words = {}
        for key, value in knowledge:
            words[key] = value
        result = []
        i = 0
        while i < n:
            if s[i] != "(":
                result.append(s[i])
                i += 1
            else:
                i += 1
                key = []
                j = i
                while j < n and s[j] != ")":
                    key.append(s[j])
                    j += 1
                key = "".join(key)
                if key in words:
                    result.append(words[key])
                else:
                    result.append("?")
                i = j + 1
        return "".join(result)
