class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtrack(row, col, i):
            if i == len(word):
                return True
                
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS
                or board[row][col] != word[i] or (row, col) in visited):
                return False

            visited.add((row, col))
            res = (backtrack(row + 1, col, i + 1) or
                    backtrack(row, col + 1, i + 1) or
                    backtrack(row - 1, col , i + 1) or
                    backtrack(row, col - 1, i + 1))
            visited.remove((row, col))
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
        return False



        