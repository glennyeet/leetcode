# Regex
import re
import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        num_strings = re.findall(r"[+-]?\d+", expression)
        nums = []
        for num in num_strings:
            nums.append(int(num))
        total_numerator = 0
        total_denominator = 1
        for i in range(0, len(nums), 2):
            numerator = nums[i]
            denominator = nums[i + 1]
            total_numerator = (
                total_numerator * denominator + numerator * total_denominator
            )
            total_denominator *= denominator
        gcd = math.gcd(total_numerator, total_denominator)
        total = str(total_numerator // gcd) + "/" + str(total_denominator // gcd)
        return total


# Parser library
# import math
# from typing import Self


# class Fraction:
#     def __init__(self, numerator: int, denominator: int):
#         self.numerator = numerator
#         self.denominator = denominator
#         self.__reduce()

#     def __reduce(self):
#         g = math.gcd(self.numerator, self.denominator)
#         self.numerator //= g
#         self.denominator //= g

#     def add(self, frac2: Self) -> Self:
#         """
#         ad + cb
#         -------
#           bd

#         """

#         new_numerator = (
#             self.numerator * frac2.denominator + frac2.numerator * self.denominator
#         )
#         new_denominator = self.denominator * frac2.denominator

#         return Fraction(new_numerator, new_denominator)

#     def subtract(self, frac2: Self) -> Self:
#         return self.add(Fraction(-1 * frac2.numerator, frac2.denominator))

#     def __str__(self) -> str:
#         return f"{self.numerator}/{self.denominator}"


# # class Parser:
# #     """
# #     expression: signed_fraction [operation expression]
# #     operation: + | -
# #     signed_fraction: sign fraction
# #     fraction = numerator / denominator
# #     sign: + | -
# #     numerator: number
# #     denominator: number
# #     number: int -> [0-9]+
# #     """

# #     def __init__(self, expression):
# #         self.index = 0
# #         self.expression = expression
# #         self.n = len(expression)

# #     def parse(self):
# #         return self.parse_expression()

# #     def parse_number(self) -> int:
# #         current = 0
# #         while self.index < self.n and self.expression[self.index].isdigit():
# #             current *= 10
# #             current += int(self.expression[self.index])
# #             self.index += 1
# #         return current

# #     def parse_operation(self) -> None | str:
# #         if self.expression[self.index] not in ["+", "-"]:
# #             return
# #         sign = self.expression[self.index]
# #         self.index += 1
# #         return sign

# #     def parse_optional_sign(self) -> None | str:
# #         if self.expression[self.index] not in ["+", "-"]:
# #             return
# #         sign = self.expression[self.index]
# #         self.index += 1
# #         return sign

# #     def parse_fraction(self) -> Fraction:
# #         numerator = self.parse_number()
# #         self.index += 1
# #         denominator = self.parse_number()
# #         return Fraction(numerator, denominator)

# #     def parse_signed_fraction(self) -> Fraction:
# #         sign = self.parse_optional_sign()
# #         fraction = self.parse_fraction()
# #         if sign == "-":
# #             fraction.numerator *= -1
# #         return fraction

# #     def parse_expression(self) -> list[Fraction | str]:
# #         fraction = self.parse_signed_fraction()
# #         expression = [fraction]
# #         if self.index < self.n:
# #             operation = self.parse_operation()
# #             expression = self.parse_expression()
# #             expression.append(operation)
# #             expression.extend(expression)
# #         return expression


# # class Solution:
# #     def fractionAddition(self, expression: str) -> str:
# #         expression = Parser(expression).parse()
# #         n = len(expression)
# #         fraction = expression[0]
# #         for i in range(1, n, 2):
# #             if expression[i] == "+":
# #                 fraction = fraction.add(expression[i + 1])
# #             else:
# #                 fraction = fraction.subract(expression[i + 1])
# #         return str(fraction)
