from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def arrange_expression(cur_cards: list[int]) -> bool:
            # Brute Force: O(1) time, O(1) space

            cur_cards_len = len(cur_cards)
            if cur_cards_len == 1:
                return abs(24 - cur_cards[0]) <= 1e-6
            for i in range(cur_cards_len):
                for j in range(i + 1, cur_cards_len):
                    new_cards = (
                        cur_cards[:i] + cur_cards[i + 1 : j] + cur_cards[j + 1 :]
                    )
                    card_a = cur_cards[i]
                    card_b = cur_cards[j]
                    new_cards.append(card_a + card_b)
                    if arrange_expression(new_cards):
                        return True
                    new_cards.pop()
                    new_cards.append(card_a - card_b)
                    if arrange_expression(new_cards):
                        return True
                    new_cards.pop()
                    new_cards.append(card_b - card_a)
                    if arrange_expression(new_cards):
                        return True
                    new_cards.pop()
                    new_cards.append(card_a * card_b)
                    if arrange_expression(new_cards):
                        return True
                    new_cards.pop()
                    if card_b != 0:
                        new_cards.append(card_a / card_b)
                        if arrange_expression(new_cards):
                            return True
                        new_cards.pop()
                    if card_a != 0:
                        new_cards.append(card_b / card_a)
                        if arrange_expression(new_cards):
                            return True
                        new_cards.pop()
            return False

        return arrange_expression(cards)
