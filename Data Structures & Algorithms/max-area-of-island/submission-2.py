class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        dirs = [[1,0], [-1, 0], [0, 1], [0, -1]]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = 1
                    grid[i][j] = 0
                    queue = collections.deque([[i,j]])

                    while queue:
                        y, x = queue.popleft()

                        for dy, dx in dirs:
                            y_, x_ = y + dy, x + dx
                            if (y_ >= 0 and y_ < ROWS
                                and x_ >= 0 and x_ < COLS
                                and grid[y_][x_] == 1):
                                queue.append([y_, x_])
                                grid[y_][x_] = 0
                                area += 1

                    max_area = max(max_area, area)
        return max_area




                    
        