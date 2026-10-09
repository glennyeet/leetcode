class Solution:
    def minInsertions(self, s: str) -> int:
        # Greedy: O(n) time, O(1) space, where n is
        # the size of s

        open_parentheses = 0
        single_right_parenthesis = False
        min_insertions = 0
        for parenthesis in s:
            if parenthesis == "(":
                if single_right_parenthesis:
                    min_insertions += 1
                    if open_parentheses == 0:
                        min_insertions += 1
                    else:
                        open_parentheses -= 1
                    single_right_parenthesis = False
                open_parentheses += 1
            else:
                if not single_right_parenthesis:
                    single_right_parenthesis = True
                else:
                    if open_parentheses > 0:
                        open_parentheses -= 1
                    else:
                        min_insertions += 1
                    single_right_parenthesis = False
        if single_right_parenthesis:
            min_insertions += 1
            if open_parentheses > 0:
                open_parentheses -= 1
            else:
                min_insertions += 1
        min_insertions += open_parentheses * 2
        return min_insertions
