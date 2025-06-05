from string import ascii_lowercase


class UnionFind:
    def __init__(self) -> None:
        self.parent = {}
        for c in ascii_lowercase:
            self.parent[c] = c

    def find(self, c: str) -> str:
        if c != self.parent[c]:
            self.parent[c] = self.find(self.parent[c])
        return self.parent[c]

    def union(self, a: str, b: str) -> str:
        a_parent = self.find(a)
        b_parent = self.find(b)
        if a_parent > b_parent:
            self.parent[a_parent] = b_parent
        else:
            self.parent[b_parent] = a_parent


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Union Find: O(m + n) time, O(n) space, where m is the size of s1
        # and n is the size of baseStr

        uf = UnionFind()
        for c1, c2 in zip(s1, s2):
            uf.union(c1, c2)
        smallest_string = []
        for c in baseStr:
            smallest_string.append(uf.find(c))
        return "".join(smallest_string)
