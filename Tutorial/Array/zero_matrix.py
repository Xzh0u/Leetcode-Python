'''编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零'''

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 保存零值的横纵坐标
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in row:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0
