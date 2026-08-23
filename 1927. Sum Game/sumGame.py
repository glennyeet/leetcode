class Solution:
    def sumGame(self, num: str) -> bool:
        # Nim: O(n) time, O(1) space

        n = len(num)
        left_question_marks = 0
        left_sum = 0
        right_question_marks = 0
        right_sum = 0
        for i in range(n // 2):
            if num[i] == "?":
                left_question_marks += 1
            else:
                left_sum += int(num[i])
        for i in range(n // 2, n):
            if num[i] == "?":
                right_question_marks += 1
            else:
                right_sum += int(num[i])
        if left_question_marks == right_question_marks:
            return left_sum != right_sum
        question_mark_delta = left_question_marks - right_question_marks
        if question_mark_delta % 2 == 1:
            return True
        sum_delta = left_sum - right_sum
        return question_mark_delta * 9 != -sum_delta * 2
