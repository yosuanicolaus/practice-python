class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[None for _ in range(n)] for _ in range(n)]
        # fill the matrix using pointer
        point = 1
        y, x = 0, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir_idx = 0
        limit = len(matrix) - 1

        while True:
            matrix[y][x] = point
            point += 1

            ay, ax = directions[curr_dir_idx]
            ny, nx = y+ay, x+ax

            if 0 <= ny <= limit and 0 <= nx <= limit and matrix[ny][nx] == None:
                y, x = ny, nx
            else:
                # occupied or out of index: change direction
                curr_dir_idx = (curr_dir_idx + 1) % 4
                ay, ax = directions[curr_dir_idx]
                ny, nx = y+ay, x+ax
                if 0 <= ny <= limit and 0 <= nx <= limit and matrix[ny][nx] == None:
                    y, x = ny, nx
                else:
                    # if still not possible, then everything is filled
                    break

        return matrix


s = Solution()
print(s.generateMatrix(1))
print(s.generateMatrix(2))
print(s.generateMatrix(3))
print(s.generateMatrix(4))
