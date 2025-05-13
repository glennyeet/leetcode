class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # Hash Map: O(t) time, O(1) space

        mod_factor = 10**9 + 7
        character_counter = [0] * 26
        for char in s:
            character_counter[ord(char) - ord("a")] += 1
        for _ in range(t):
            new_character_counter = [0] * 26
            for i in range(26):
                if i == 25:
                    new_character_counter[0] = (
                        new_character_counter[0] + character_counter[i]
                    ) % mod_factor
                    new_character_counter[1] = (
                        new_character_counter[1] + character_counter[i]
                    ) % mod_factor
                else:
                    new_character_counter[i + 1] = character_counter[i] % mod_factor
            character_counter = new_character_counter
        result_length = 0
        for count in character_counter:
            result_length = (result_length + count) % mod_factor
        return result_length
