class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = defaultdict(bool) # map (y, x) -> bool

        height = len(grid)
        length = len(grid[0])

        queue = deque()

        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        num = 0
        for row in range(height):
            for col in range(length):
                if grid[row][col] == "1" and not visited[(row, col)]:
                    # run bfs
                    queue.append((row, col))
                    visited[(row, col)] = True

                    while queue:
                        curr_row, curr_col = queue.popleft()

                        # add neighbors
                        for y, x in DIRS:
                            new_row = curr_row + y
                            new_col = curr_col + x

                            if new_row < height and new_col < length and new_row >= 0 and new_col >= 0 and grid[new_row][new_col] == "1" and not visited[(new_row, new_col)]:
                                queue.append((new_row, new_col))
                                visited[(new_row, new_col)] = True

                    num += 1
        return num

        