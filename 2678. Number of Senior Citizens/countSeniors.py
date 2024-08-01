class Solution:
    def countSeniors(self, details: List[str]) -> int:
        old = 0
        for senior in details:
            if int(senior[11:13]) > 60:
                old += 1
        return old
