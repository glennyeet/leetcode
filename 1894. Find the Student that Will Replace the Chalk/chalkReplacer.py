class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_students = len(chalk)
        k_remainder = k % sum(chalk)
        student = 0
        i = 0
        while k_remainder >= 0:
            student = i % total_students
            k_remainder -= chalk[student]
            i += 1
        return student
