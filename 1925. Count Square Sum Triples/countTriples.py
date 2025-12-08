from math import sqrt


class Solution:
    def countTriples(self, n: int) -> int:
        # Math + Enumeration: O(n^2) time,
        # O(1) space

        square_triples = 0
        for a in range(1, n):
            for b in range(a, n):
                c = sqrt(a**2 + b**2)
                if c > n:
                    break
                elif c.is_integer():
                    if a == b:
                        square_triples += 1
                    else:
                        square_triples += 2
        return square_triples
