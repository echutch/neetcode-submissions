class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i, j = 0, len(matrix) - 1

        while i < j:
            for col in range(len(matrix)):
                top = matrix[i][col]
                bottom = matrix[j][col]

                matrix[i][col] = bottom
                matrix[j][col] = top
            i += 1
            j -= 1

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                upper = matrix[i][j]
                lower = matrix[j][i]

                matrix[i][j] = lower
                matrix[j][i] = upper
        
        
        # [7, 8, 9]
        # [4, 5, 6]
        # [1, 2, 3]