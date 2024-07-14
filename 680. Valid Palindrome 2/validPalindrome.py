class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        deleted = False
        while i < j:
            if s[i] != s[j] and not deleted:
                deleted = True
                break
            else:
                i += 1
                j -= 1
        if not deleted:
            return True
        # k = i
        # l = j - 1
        # valid = True
        # while k < l:
        #     if s[k] != s[l]:
        #         valid = False
        #         break
        #     k += 1
        #     l -= 1
        # if valid:
        #     return True
        # k = i + 1
        # l = j
        # valid = True
        # while k < l:
        #     if s[k] != s[l]:
        #         valid = False
        #         break
        #     k += 1
        #     l -= 1
        # if valid:
        #     return True
        # return False
        subString1 = s[0:i] + s[i + 1 :]
        subString2 = s[0:j] + s[j + 1 :]
        return subString1 == subString1[::-1] or subString2 == subString2[::-1]
