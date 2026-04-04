class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # Simulation: O(n) time, O(n) space

        n = len(encodedText)
        cols = n // rows
        encoded_matrix = [[None] * cols for _ in range(rows)]
        for i, char in enumerate(encodedText):
            encoded_matrix[i // cols][i % cols] = char
        original_text = []
        for i in range(cols):
            for j in range(rows):
                if i + j < cols:
                    original_text.append(encoded_matrix[j][i + j])
        return "".join(original_text).rstrip()
