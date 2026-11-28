class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = []

        up = 0
        down = ROWS - 1
        left = 0
        right = COLS - 1

        while up <= down and left <= right:
            for col in range(left, right + 1):
                res.append(matrix[up][col])
            up += 1

            for row in range(up, down + 1):
                res.append(matrix[row][right])
            right -= 1

            if up <= down:
                for col in range(right, left - 1, -1):
                    res.append(matrix[down][col])
                down -= 1

            if left <= right:
                for row in range(down, up - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
        