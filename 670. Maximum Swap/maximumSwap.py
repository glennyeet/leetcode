class Solution:
    def maximumSwap(self, num: int) -> int:
        max_number = num
        num_list = list(str(num))
        num_len = len(num_list)
        for i in range(num_len):
            for j in range(i + 1, num_len):
                new_num = num_list.copy()
                new_num[i], new_num[j] = new_num[j], new_num[i]
                new_num = int("".join(new_num))
                max_number = max(max_number, new_num)
        return max_number
