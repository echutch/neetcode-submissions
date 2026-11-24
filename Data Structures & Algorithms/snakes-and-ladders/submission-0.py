from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def sqToPos(sq):
            row = (sq - 1) // n
            col = (sq - 1) % n

            if row % 2 == 1:
                col = n - 1 - col
            row = n - 1 - row
            return row, col
        
        queue = deque()
        queue.append(1)

        first_row, first_col = sqToPos(1)
        board[first_row][first_col] = 0

        jumps = 0
        while queue:
            level = len(queue)
            jumps += 1

            for _ in range(level):
                curr = queue.popleft()
                
                for i in range(1, 7):
                    next = curr + i
                    if next > n*n:
                        break

                    row, col = sqToPos(next)
                    if board[row][col] != -1:
                        next = board[row][col]

                    if board[row][col] != 0:
                        if next == n*n:
                            return jumps
                        queue.append(next)
                        board[row][col] = 0
        return -1
                        


