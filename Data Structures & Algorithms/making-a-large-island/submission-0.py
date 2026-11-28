from collections import defaultdict, deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_size = defaultdict(int)

        ROWS = len(grid)
        COLS = len(grid[0])

        id = 2
        max_size = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    queue = deque()
                    queue.append((row, col))
                    grid[row][col] = id
                    size = 1

                    while queue:
                        curr_row, curr_col = queue.popleft()

                        dirs = [(curr_row + 1, curr_col), (curr_row - 1, curr_col), (curr_row, curr_col + 1), (curr_row, curr_col - 1)]

                        for new_row, new_col in dirs:
                            if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1:
                                queue.append((new_row, new_col))
                                grid[new_row][new_col] = id
                                size += 1
                    max_size = max(max_size, size)
                    island_size[id] = size
                    id += 1
        

        for curr_row in range(ROWS):
            for curr_col in range(COLS):
                if grid[curr_row][curr_col] == 0:
                    dirs = [(curr_row + 1, curr_col), (curr_row - 1, curr_col), (curr_row, curr_col + 1), (curr_row, curr_col - 1)]

                    curr_size = 1
                    seen = set()
                    for new_row, new_col in dirs:
                        if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] not in seen:
                            id = grid[new_row][new_col]
                            seen.add(id)
                            curr_size += island_size[id]
                    max_size = max(max_size, curr_size)
        return max_size
                            
                    
                    

