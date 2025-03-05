class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [['?'] * cols for _ in range(rows)]

    def __str__(self):
        return '\n'.join(''.join(str(cell) for cell in row) for row in self.data)

    def __getitem__(self, index):
        row, col = index
        return self.data[row][col]
    
    def __setitem__(self, index, value):
        row, col = index
        self.data[row][col] = value
