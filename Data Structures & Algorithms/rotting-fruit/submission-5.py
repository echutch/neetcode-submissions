class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        count_fresh = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    count_fresh += 1

        time = 0
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while count_fresh > 0 and queue:
            level = len(queue)
            for _ in range(level):
                curr_row, curr_col = queue.popleft()

                for dy, dx in DIRS:
                    new_row, new_col = curr_row + dy, curr_col + dx

                    if new_row < ROWS and new_col < COLS and new_row >= 0 and new_col >= 0 and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        count_fresh -= 1
                        queue.append((new_row, new_col))
            time += 1
        
        if count_fresh == 0:
            return time
        else:
            return -1



        