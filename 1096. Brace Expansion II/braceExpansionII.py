class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Backtracking: O(n * 2^(n / 5)) time, O(n * 2^(n / 5))
        # space

        n = len(expression)

        def eval(start: int, end: int) -> set[str]:
            if start == end:
                return set([expression[start]])
            unions = []
            segment_start = start
            depth = 0
            for i in range(start, end + 1):
                if expression[i] == "{":
                    depth += 1
                elif expression[i] == "}":
                    depth -= 1
                else:
                    if expression[i] == "," and depth == 0:
                        unions.append(eval(segment_start, i - 1))
                        segment_start = i + 1
            if len(unions) > 0:
                unions.append(eval(segment_start, end))
                result = set()
                for union in unions:
                    result |= union
                return result
            result = set([""])
            depth = 0
            for i in range(start, end + 1):
                if expression[i] == "{":
                    if depth == 0:
                        segment_start = i + 1
                    depth += 1
                elif expression[i] == "}":
                    depth -= 1
                    if depth == 0:
                        current = eval(segment_start, i - 1)
                        combined_result = set()
                        for a in result:
                            for b in current:
                                combined_result.add(a + b)
                        result = combined_result
                else:
                    if depth == 0:
                        combined_result = set()
                        for a in result:
                            combined_result.add(a + expression[i])
                        result = combined_result
            return result

        result = eval(0, n - 1)
        return list(sorted(result))
