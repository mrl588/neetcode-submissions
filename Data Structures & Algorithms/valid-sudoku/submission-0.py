class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        squares = [[] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                box = (row // 3) * 3 + (col // 3)
                if val != '.':
                    if val in rows[row] or val in cols[col] or val in squares[box]:
                        return False
                    rows[row].append(val)
                    cols[col].append(val)
                    squares[box].append(val)
        return True

        