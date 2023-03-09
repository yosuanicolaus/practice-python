from collections import deque


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        queue = deque()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 1)]
        total_layer_trip = len(matrix) // 2
        trip_len = len(matrix) - 1
        ny, nx = 1, 1
        y, x = 0, 0

        for _ in range(total_layer_trip):
            for i in range(len(directions)):
                ay, ax = directions[i]
                for _ in range(trip_len):
                    if i == 0:
                        # just queue
                        queue.append(matrix[y][x])
                    elif i == 4:
                        # just replace
                        matrix[y][x] = queue.popleft()
                    else:
                        queue.append(matrix[y][x])
                        matrix[y][x] = queue.popleft()
                    y, x = y+ay, x+ax
            trip_len -= 2
            y, x, ny, nx = ny, nx, ny+1, nx+1


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s = Solution()
s.rotate(matrix)
print(matrix)
