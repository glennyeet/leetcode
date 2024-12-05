class Solution:
    def canChange(self, start: str, target: str) -> bool:
        l = 0
        for r in range(len(target)):
            if target[r] == "_":
                continue
            while l < len(start) and start[l] == "_":
                l += 1
            if l == len(start):
                return False
            if (
                target[r] != start[l]
                or target[r] == "L"
                and l < r
                or target[r] == "R"
                and l > r
            ):
                return False
            l += 1
        while l < len(start):
            if start[l] != "_":
                return False
            l += 1
        return True
