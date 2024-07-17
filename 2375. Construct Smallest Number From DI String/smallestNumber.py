class Solution:
    def smallestNumber(self, pattern: str) -> str:
        number = [1]
        for c in pattern:
            if c == "I":
                i = 1
                while i in number:
                    i += 1
                number.append(i) 
            else:
                number.append(number[-1])
                i = len(number) - 2
                while i >= 0 and number[i] == number[i + 1]:
                    number[i] += 1
                    i -= 1
        number = "".join([str(d) for d in number])
        return number
