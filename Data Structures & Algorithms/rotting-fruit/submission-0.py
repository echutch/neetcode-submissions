class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()
        dist = {}
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    dist[(i,j)] = 0
                elif grid[i][j] == 1:
                    fresh += 1


        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        time = 0
        while queue:
            y, x = queue.popleft()

            for dy, dx in dirs:
                y_, x_ = y + dy, x + dx
                if (y_ >= 0 and y_ < ROWS
                    and x_ >= 0 and x_ < COLS
                    and grid[y_][x_] == 1):
                    queue.append((y_, x_))
                    grid[y_][x_] = 2
                    dist[(y_, x_)] = 1 + dist[(y, x)]
                    time = max(time, dist[(y_, x_)])
                    fresh -= 1
        
        return time if fresh == 0 else -1
            
        



        