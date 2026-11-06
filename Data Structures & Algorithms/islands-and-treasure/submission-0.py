class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        queue = collections.deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            y, x = queue.popleft()

            for dy, dx in dirs:
                y_, x_ = y + dy, x + dx
                if (y_ >= 0 and y_ < ROWS
                    and x_ >= 0 and x_ < COLS
                    and grid[y_][x_] != -1 and (y_, x_) not in visited):
                    queue.append((y_, x_))
                    visited.add((y_, x_))
                    grid[y_][x_] = 1 + grid[y][x]

        