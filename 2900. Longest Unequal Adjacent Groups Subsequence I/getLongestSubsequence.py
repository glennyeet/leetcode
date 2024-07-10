class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prevGroup = -1
        maxSubSeq = []
        for i in range(len(words)):
            if groups[i] != prevGroup:
                maxSubSeq.append(words[i])
                prevGroup = groups[i]
        return maxSubSeq
