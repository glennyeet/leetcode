class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s = list(s)
        lastSeen = {}
        for i in range(len(s)):
            lastSeen[s[i]] = i
        partitionSizes = []
        i = j = 0
        while i < len(s):
            j = lastSeen[s[i]]
            k = 0
            while k < j:
                if lastSeen[s[k]] > j:
                    j = lastSeen[s[k]]
                k += 1
            partitionSizes.append(j - i + 1)
            i = j + 1
        return partitionSizes
