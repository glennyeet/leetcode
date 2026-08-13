from sortedcontainers import SortedList, SortedSet
from typing import List


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        # Ordered Set: O(k * log(n)) time, O(n) space

        n = len(s)
        k = len(queryCharacters)
        s_chars = list(s)
        run_starts = SortedSet()
        for i in range(n):
            if i == 0 or s_chars[i - 1] != s_chars[i]:
                run_starts.add(i)
        boundaries = list(run_starts)
        boundaries.append(n)
        candidates = SortedList()
        for a, b in zip(boundaries, boundaries[1:]):
            candidates.add((b - a, a))
        lengths = [None] * k
        for i, (qc, qi) in enumerate(zip(queryCharacters, queryIndices)):
            if s_chars[qi] == qc:
                if i == 0:
                    lengths[i] = candidates[-1][0]
                else:
                    lengths[i] = lengths[i - 1]
                continue
            ri = run_starts.bisect_right(qi) - 1
            if s_chars[run_starts[ri]] != qc:
                run_starts.add(qi)
            if qi + 1 < n and s_chars[qi + 1] != qc:
                run_starts.add(qi + 1)
            ri = run_starts.bisect_right(qi) - 1
            stale_starts = []
            if ri > 0 and s_chars[run_starts[ri - 1]] == qc:
                stale_starts.append(qi)
            if ri + 1 < len(run_starts) and s_chars[run_starts[ri + 1]] == qc:
                stale_starts.append(run_starts[ri + 1])
            for start in stale_starts:
                run_starts.remove(start)
            for j in range(ri - 2, ri + 2):
                if 0 <= j < len(run_starts):
                    if j + 1 < len(run_starts):
                        length = run_starts[j + 1] - run_starts[j]
                    else:
                        length = n - run_starts[j]
                    candidates.add((length, run_starts[j]))
            s_chars[qi] = qc
            found = False
            while not found:
                length, ci = candidates[-1]
                ri = run_starts.bisect_left(ci)
                if ri == len(run_starts) or run_starts[ri] != ci:
                    candidates.remove(candidates[-1])
                    continue
                if ri + 1 < len(run_starts):
                    if length == run_starts[ri + 1] - run_starts[ri]:
                        found = True
                        lengths[i] = length
                        break
                    else:
                        candidates.remove(candidates[-1])
                        continue
                else:
                    if length == n - run_starts[ri]:
                        found = True
                        lengths[i] = length
                        break
                    else:
                        candidates.remove(candidates[-1])
                        continue
        return lengths
