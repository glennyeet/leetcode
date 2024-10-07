class Solution:
    def minLength(self, s: str) -> int:
        # Brute force
        # s_len = len(s)
        # if s_len == 1:
        #     return 1
        # min_len = s_len
        # s_arr = list(s)
        # while True:
        #     new_s_arr = []
        #     cur_len = min_len
        #     s_arr_len = len(s_arr)
        #     for i in range(s_arr_len):
        #         if i < s_arr_len - 1 and (
        #             s_arr[i] == "A"
        #             and s_arr[i + 1] == "B"
        #             or s_arr[i] == "C"
        #             and s_arr[i + 1] == "D"
        #         ):
        #             min_len -= 1
        #         elif i > 0 and (
        #             s_arr[i] == "B"
        #             and s_arr[i - 1] == "A"
        #             or s_arr[i] == "D"
        #             and s_arr[i - 1] == "C"
        #         ):
        #             min_len -= 1
        #         else:
        #             new_s_arr.append(s_arr[i])
        #     if min_len == cur_len:
        #         return min_len
        #     s_arr = new_s_arr

        # Stack
        chars = []
        for c in s:
            if len(chars) == 0:
                chars.append(c)
            elif c == "B" and chars[-1] == "A" or c == "D" and chars[-1] == "C":
                chars.pop()
            else:
                chars.append(c)
        return len(chars)
