class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # Bracket Sequences: O(n) time, O(n) space

        n = len(seq)
        max_depth = 0
        cur_depth = 0
        for bracket in seq:
            if bracket == "(":
                cur_depth += 1
                max_depth = max(max_depth, cur_depth)
            else:
                cur_depth -= 1
        A_depth = max_depth // 2
        answer = [None] * n
        cur_depth = 0
        for i, bracket in enumerate(seq):
            if bracket == "(":
                if cur_depth + 1 <= A_depth:
                    answer[i] = 0
                    cur_depth += 1
                else:
                    answer[i] = 1
            else:
                if cur_depth - 1 >= 0:
                    answer[i] = 0
                    cur_depth -= 1
                else:
                    answer[i] = 1
        return answer
