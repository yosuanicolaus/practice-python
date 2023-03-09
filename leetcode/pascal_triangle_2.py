class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row: list[int] = [1]

        for _ in range(rowIndex):
            a, b = 0, 1
            row_copy = [*row]
            while b < len(row):
                row[b] = row_copy[a] + row_copy[b]
                a, b = a+1, b+1
            row.append(1)

        return row


s = Solution()
print(s.getRow(0))
print(s.getRow(1))
print(s.getRow(2))
print(s.getRow(3))
print(s.getRow(4))
print(s.getRow(5))
