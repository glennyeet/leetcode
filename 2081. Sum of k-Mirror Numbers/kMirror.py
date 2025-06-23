class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # Enumeration: O(1) time, O(1) space

        def is_k_mirror_num(num: int) -> bool:
            base_k_num = []
            while num:
                base_k_num.append(num % k)
                num //= k
            return base_k_num == base_k_num[::-1]

        k_mirror_nums = 0
        k_mirror_nums_sum = 0
        left = 1
        while k_mirror_nums < n:
            right = left * 10
            for first_half in range(left, right):
                if k_mirror_nums == n:
                    break
                cur_num = first_half
                second_half = first_half // 10
                while second_half:
                    cur_num = cur_num * 10 + second_half % 10
                    second_half //= 10
                if is_k_mirror_num(cur_num):
                    k_mirror_nums += 1
                    k_mirror_nums_sum += cur_num
            for first_half in range(left, right):
                if k_mirror_nums == n:
                    break
                cur_num = first_half
                second_half = first_half
                while second_half:
                    cur_num = cur_num * 10 + second_half % 10
                    second_half //= 10
                if is_k_mirror_num(cur_num):
                    k_mirror_nums += 1
                    k_mirror_nums_sum += cur_num
            left = right
        return k_mirror_nums_sum
