#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        tr = - 1
        while l < r:
            m = l + (r - l) // 2

            if m+1 < len(matrix) and matrix[m][0] < target < matrix[m+1][0]:
                tr = m
                break
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                l = m + 1
            else:
                return True

        if l == r:
            tr = l
        l, r = 0, len(matrix[tr]) - 1

        while l <= r:
            m = l + (r - l) // 2

            if matrix[tr][m] < target:
                l = m+1
            elif matrix[tr][m] > target:
                r = m - 1
            else:
                return True

        return False

# @lc code=end


s = Solution()
s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
