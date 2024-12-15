from heapq import heapify, heappushpop


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        p_queue = []
        for class_pass, class_total in classes:
            pass_ratio_increase = (class_pass + 1) / (
                class_total + 1
            ) - class_pass / class_total
            p_queue.append((-pass_ratio_increase, class_pass, class_total))
        heapify(p_queue)
        extra_students_assigned = 0
        while extra_students_assigned < extraStudents:
            extra_students_assigned += 1
            pass_ratio_increase, class_pass, class_total = p_queue[0]
            new_class_pass = class_pass + 1
            new_class_total = class_total + 1
            new_pass_ratio_increase = (new_class_pass + 1) / (
                new_class_total + 1
            ) - new_class_pass / new_class_total
            heappushpop(
                p_queue, (-new_pass_ratio_increase, new_class_pass, new_class_total)
            )
        pass_ratio_sum = 0
        for _, class_pass, class_total in p_queue:
            pass_ratio_sum += class_pass / class_total
        return pass_ratio_sum / len(p_queue)
