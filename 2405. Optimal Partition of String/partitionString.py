class Solution:
    def partitionString(self, s: str) -> int:
        # s = list(s)
        # lastSeen = {}
        # substrings = i = 0
        # while i < len(s):
        #     if s[i] not in lastSeen.keys():
        #         lastSeen[s[i]] = i
        #     else:
        #         substrings += 1
        #         lastSeen = {s[i]: i}
        #     i += 1
        # substrings += 1
        # return substrings

        # lastSeen = set()
        # substrings = 1
        # for c in s:
        #     if c not in lastSeen:
        #         lastSeen.add(c)
        #     else:
        #         substrings += 1
        #         lastSeen = {c}
        # return substrings

        # lastSeen = []
        # substrings = 1
        # for c in s:
        #     if c not in lastSeen:
        #         lastSeen.append(c)
        #     else:
        #         substrings += 1
        #         lastSeen = [c]
        # return substrings

        lastSeen = ""
        substrings = 1
        for c in s:
            if c not in lastSeen:
                lastSeen += c
            else:
                substrings += 1
                lastSeen = c
        return substrings
