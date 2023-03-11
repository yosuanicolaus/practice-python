class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = m and len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True

        return False


s = Solution()
print(s.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
      3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20))
print(s.searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [
      3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))
print(s.searchMatrix([[-5]], -2))
