class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pac_grid = [[False] * COLS for _ in range(ROWS)] 
        atl_grid = [[False] * COLS for _ in range(ROWS)] 

        def bfs(queue, heights, grid):
            DIRS = ((1,0), (-1,0), (0,1), (0,-1))

            while queue:
                row, col = queue.popleft()

                for dy, dx in DIRS:
                    new_row, new_col = row + dy, col + dx

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and not grid[new_row][new_col] and heights[new_row][new_col] >= heights[row][col]:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = True

        pac_queue = deque()
        atl_queue = deque()

        for col in range(COLS):
            pac_queue.append((0, col))
            pac_grid[0][col] = True
            atl_queue.append((ROWS - 1, col))
            atl_grid[ROWS-1][col] = True

        for row in range(ROWS):
            pac_queue.append((row, 0))
            pac_grid[row][0] = True
            atl_queue.append((row, COLS - 1))
            atl_grid[row][COLS-1] = True


        bfs(pac_queue, heights, pac_grid)
        bfs(atl_queue, heights, atl_grid)

        # print(pac_grid)
        # print()
        # print(atl_grid)

        out = []

        for row in range(ROWS):
            for col in range(COLS):
                if pac_grid[row][col] and atl_grid[row][col]:
                    out.append([row, col])
        return out

            

        