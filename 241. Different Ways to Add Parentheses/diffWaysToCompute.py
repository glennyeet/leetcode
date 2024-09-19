from itertools import groupby


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums_and_ops = []
        for is_op, t in groupby(expression, lambda x: x in "+-*"):
            if is_op:
                nums_and_ops.append(list(t)[0])
            else:
                nums_and_ops.append(int("".join(list(t))))

        def calculate(left: int, right: int) -> int:
            if left == right:
                return [nums_and_ops[left]]
            res = []
            for op_index in range(left + 1, right, 2):
                left_calc = calculate(left, op_index - 1)
                right_calc = calculate(op_index + 1, right)
                match nums_and_ops[op_index]:
                    case "+":
                        for left_num in left_calc:
                            for right_num in right_calc:
                                res.append(left_num + right_num)
                    case "-":
                        for left_num in left_calc:
                            for right_num in right_calc:
                                res.append(left_num - right_num)
                    case "*":
                        for left_num in left_calc:
                            for right_num in right_calc:
                                res.append(left_num * right_num)
            return res

        return calculate(0, len(nums_and_ops) - 1)
