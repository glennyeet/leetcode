from collections import Counter


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Hash map: O(n) time, O(n) space

        ball_to_colour = {}
        colour_counter = Counter()
        distinct_colours = 0
        result = []
        for x, y in queries:
            if x in ball_to_colour:
                old_colour = ball_to_colour[x]
                colour_counter[old_colour] -= 1
                if colour_counter[old_colour] == 0:
                    distinct_colours -= 1
            ball_to_colour[x] = y
            if colour_counter[y] == 0:
                distinct_colours += 1
            colour_counter[y] += 1
            result.append(distinct_colours)
        return result
