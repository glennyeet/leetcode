class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Math + Hash Table: O(ϕ(|d|)) time, O(|d|) space, where ϕ(x) is
        # Euler's totient function and d is denominator

        if numerator == 0:
            return "0"
        quotient = []
        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            quotient.append("-")
        dividend = abs(numerator)
        divisor = abs(denominator)
        quotient.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(quotient)
        quotient.append(".")
        decimal = []
        remainders = {}
        opening_parantheses_index = 0
        while remainder != 0:
            if remainder in remainders:
                decimal.insert(remainders[remainder], "(")
                decimal.append(")")
                break
            remainders[remainder] = opening_parantheses_index
            remainder *= 10
            decimal.append(str(remainder // divisor))
            remainder %= divisor
            opening_parantheses_index += 1
        quotient.extend(decimal)
        return "".join(quotient)
