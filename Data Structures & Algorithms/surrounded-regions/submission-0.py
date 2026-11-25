class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if (row == 0 or row == ROWS - 1 or col == 0 or col == COLS - 1) and board[row][col] == "O":
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            board[row][col] = "T"

            dirs = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for new_row, new_col in dirs:
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and board[new_row][new_col] == "O":
                    queue.append((new_row, new_col))

        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"
