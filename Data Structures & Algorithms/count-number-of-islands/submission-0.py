class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1

                    stack = [[i, j]]
                    while stack:
                        y, x = stack.pop()
                        grid[y][x] = '0'
                        
                        if y > 0 and grid[y-1][x] == '1':
                            stack.append([y-1,x])
                        if y < len(grid) - 1 and grid[y+1][x] == '1':
                            stack.append([y+1,x])
                        if x > 0 and grid[y][x-1] == '1':
                            stack.append([y, x-1])
                        if x < len(grid[0]) - 1 and grid[y][x+1] == '1':
                            stack.append([y, x+1])
        return count





    

        