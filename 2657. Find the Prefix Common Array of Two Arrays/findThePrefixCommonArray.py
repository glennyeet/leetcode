class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Hash set: O(n) time, O(n) space, where n is the size of A

        a_visited = set()
        b_visited = set()
        prefix_common_array = []
        common_count = 0
        for a, b in zip(A, B):
            a_visited.add(a)
            b_visited.add(b)
            if a in b_visited:
                common_count += 1
            if b in a_visited and a != b:
                common_count += 1
            prefix_common_array.append(common_count)
        return prefix_common_array
