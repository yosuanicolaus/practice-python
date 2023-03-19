#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        stack = [(sr, sc)]
        start_color = image[sr][sc]

        if start_color == color:
            return image
        image[sr][sc] = color

        while stack != []:
            r, c = stack.pop()
            if r - 1 >= 0 and image[r-1][c] == start_color:
                image[r-1][c] = color
                stack.append((r-1, c))
            if r + 1 < len(image) and image[r+1][c] == start_color:
                image[r+1][c] = color
                stack.append((r+1, c))
            if c - 1 >= 0 and image[r][c-1] == start_color:
                image[r][c-1] = color
                stack.append((r, c-1))
            if c + 1 < len(image[0]) and image[r][c+1] == start_color:
                image[r][c+1] = color
                stack.append((r, c+1))

        return image


# @lc code=end
