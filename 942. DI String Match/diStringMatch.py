class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # nums = [*range(len(s) + 1)]
        # perm = []
        # for c in s:
        #     if c == 'I':
        #         perm.append(nums.pop(0))
        #     else:
        #         perm.append(nums.pop(len(nums) - 1))
        # perm.append(nums.pop(0))
        # return perm
        d = len(s)
        i = 0
        perm = []
        for c in s:
            if c == 'D':
                perm.append(d)
                d -= 1
            else:
                perm.append(i)
                i += 1
        perm.append(i)
        return perm
