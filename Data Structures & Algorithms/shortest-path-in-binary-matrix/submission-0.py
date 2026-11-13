class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        queue = deque()
        queue.append((0,0))
        grid[0][0] = 1

        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        count = 0
        while queue:
            count += 1
            level = len(queue)
            
            for _ in range(level):
                row, col = queue.popleft()

                if row == ROWS - 1 and col == COLS - 1:
                    return count

                for dy, dx in DIRS:
                    new_row = dy + row
                    new_col = dx + col

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 0:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 1

        return -1
            
        