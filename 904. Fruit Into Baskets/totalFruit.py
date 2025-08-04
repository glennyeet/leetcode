from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Hash Table: O(n) time, O(n) space, where
        # n is the size of fruits

        baskets = []
        last_position = {}
        cur_fruits = 0
        max_fruits = 0
        for i, fruit in enumerate(fruits):
            last_position[fruit] = i
            if fruit not in baskets:
                baskets.append(fruit)
                if len(baskets) > 2:
                    max_fruits = max(max_fruits, cur_fruits)
                    removed_fruit_position = float("inf")
                    for fruit in baskets:
                        if last_position[fruit] < removed_fruit_position:
                            removed_fruit_position = last_position[fruit]
                            removed_fruit = fruit
                    baskets.remove(removed_fruit)
                    cur_fruits = i - removed_fruit_position - 1
            cur_fruits += 1
        max_fruits = max(max_fruits, cur_fruits)
        return max_fruits
