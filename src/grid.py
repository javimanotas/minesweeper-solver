from typing import *

class Grid:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = [['?'] * cols for _ in range(rows)]

    def __str__(self) -> str:
        return '\n'.join(''.join(str(cell) for cell in row) for row in self.data)

    def __getitem__(self, index: Tuple[int, int]) -> int | str:
        row, col = index
        return self.data[row][col]
    
    def __setitem__(self, index: Tuple[int, int], value: int | str):
        row, col = index
        self.data[row][col] = value
