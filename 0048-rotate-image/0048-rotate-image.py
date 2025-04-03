class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose_in_place(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i + 1, n):  # Swap only upper triangle elements
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        

        transpose_in_place(matrix)
        for row in matrix:
            row.reverse()
        
        return matrix