from heapq import heappush, heappop, heapify


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        if a == b == c == 0:
            return ""
        letter_counts = []
        if a > 0:
            letter_counts.append((-a, "a"))
        if b > 0:
            letter_counts.append((-b, "b"))
        if c > 0:
            letter_counts.append((-c, "c"))
        heapify(letter_counts)
        happy_string = ""
        while letter_counts:
            left, letter = heappop(letter_counts)
            if len(happy_string) > 1 and happy_string[-2] == happy_string[-1] == letter:
                if not letter_counts:
                    break
                delimiter_left, delimiter = heappop(letter_counts)
                delimiter_left += 1
                happy_string += delimiter
                if delimiter_left < 0:
                    heappush(letter_counts, (delimiter_left, delimiter))
            else:
                left += 1
                happy_string += letter
            if left < 0:
                heappush(letter_counts, (left, letter))
        return happy_string
