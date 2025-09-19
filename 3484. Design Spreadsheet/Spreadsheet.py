class Spreadsheet:
    # Matrix + String

    def __init__(self, rows: int):
        # O(n) time, O(n) space, where n is the number
        # of rows

        self.cells = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        # O(1) time, O(1) space

        row = int(cell[1:]) - 1
        col = ord(cell[0]) - ord("A")
        self.cells[row][col] = value

    def resetCell(self, cell: str) -> None:
        # O(1) time, O(1) space

        row = int(cell[1:]) - 1
        col = ord(cell[0]) - ord("A")
        self.cells[row][col] = 0

    def getValue(self, formula: str) -> int:
        # O(1) time, O(1) space

        X, Y = formula[1:].split("+")
        if X[0].isalpha():
            row1 = int(X[1:]) - 1
            col1 = ord(X[0]) - ord("A")
            X_value = self.cells[row1][col1]
        else:
            X_value = int(X)
        if Y[0].isalpha():
            row2 = int(Y[1:]) - 1
            col2 = ord(Y[0]) - ord("A")
            Y_value = self.cells[row2][col2]
        else:
            Y_value = int(Y)
        return X_value + Y_value


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
