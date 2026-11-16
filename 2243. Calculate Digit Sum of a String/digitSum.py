class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # Simulation: O(m) time, O(m) space,
        # where m is the size of s

        final_s = s
        while len(final_s) > k:
            n = len(final_s)
            new_s = []
            group_sum = 0
            for i in range(n):
                if i % k == 0 and i // k > 0:
                    new_s.append(str(group_sum))
                    group_sum = 0
                group_sum += int(final_s[i])
                if i == n - 1:
                    new_s.append(str(group_sum))
            final_s = "".join(new_s)
        return final_s
