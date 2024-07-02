class Solution:
    def maximum69Number (self, num: int) -> int:
        # digits = []
        # while num > 0:
        #     digit = num % 10
        #     digits = [digit] + digits
        #     num //= 10
        # for i in range(len(digits)):
        #     if digits[i] == 6:
        #         digits[i] = 9
        #         break
        # max_number = int(''.join(str(x) for x in digits))
        # return max_number
        digits = [d for d in str(num)]
        for i in range(len(digits)):
            if digits[i] == '6':
                digits[i] = '9'
                break
        max_number = int(''.join(digits))
        return max_number
