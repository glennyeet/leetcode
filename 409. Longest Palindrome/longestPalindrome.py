class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        maxLength = 0
        oddOccurenceChar = False
        for c in counter:
            occurrences = counter[c]
            if not oddOccurenceChar and occurrences % 2 == 1:
                maxLength += occurrences
                oddOccurenceChar = True
            elif occurrences >= 2:
                if occurrences % 2 == 0:
                    maxLength += occurrences
                else:
                    maxLength += occurrences - 1
        return maxLength
