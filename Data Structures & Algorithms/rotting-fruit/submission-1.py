class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        dist = {}

        fresh = 0

        for y in range(ROWS):
            for x in range(COLS):
                if grid[y][x] == 2:
                    q.append((x, y))
                    dist[(x, y)] = 0
                elif grid[y][x] == 1:
                    fresh += 1

        time = 0
        while q:
            i, j = q.popleft()

            for dx, dy in DIRS:
                x, y = i + dx, j + dy
                
                if x >= 0 and y >= 0 and x < COLS and y < ROWS and grid[y][x] == 1:
                    grid[y][x] = 2
                    dist[(x, y)] = 1 + dist[(i, j)]
                    time = max(time, dist[(x, y)])
                    q.append((x, y))
                    fresh -= 1
        return time if fresh == 0 else -1




                    



            

            

            
        



        