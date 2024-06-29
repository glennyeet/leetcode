class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        charCount = {}
        kLeft = k
        maxChar = s[0]

        while end != len(s):
            endC = s[end]
            
            if endC in charCount:
                charCount[endC] += 1
            else:
                charCount[endC] = 1
            
            if endC != maxChar:
                kLeft -= 1

                if charCount[endC] > charCount[maxChar]:
                    kLeft += charCount[endC] - charCount[maxChar]
                    maxChar = endC
            
            if kLeft < 0:
                startC = s[start]
                charCount[startC] -= 1
                if startC != maxChar:
                    kLeft += 1
                start += 1
            
            # print('max char', maxChar, 'start', start, 'end', end, 'k left', kLeft)
            # print('char count', charCount)

            end += 1

        maxLength = end - start

        return maxLength
