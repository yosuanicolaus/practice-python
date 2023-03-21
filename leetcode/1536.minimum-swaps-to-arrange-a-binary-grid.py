#
# @lc app=leetcode id=1536 lang=python3
#
# [1536] Minimum Swaps to Arrange a Binary Grid
#

# @lc code=start
class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        # count each row, how many zeros from the right does it have
        # check each row if it already meets the requirement.
        # if not yet, look at other row that can meet it, if not found, return -1
        # if found, bubble swap that row to the current row
        # continue, if the for loop finishes, return num of swap

        trails = []
        swap = 0

        for row in grid:
            count = 0
            for num in row[::-1]:
                if num == 0:
                    count += 1
                else:
                    break
            trails.append(count)

        for i in range(len(trails) - 1):
            req = len(grid) - 1 - i

            if trails[i] >= req:
                continue

            found = False
            for j in range(i + 1, len(trails)):
                if trails[j] >= req:
                    found = True
                    while j > i:
                        trails[j], trails[j-1] = trails[j-1], trails[j]
                        swap += 1
                        j -= 1
                    break

            if not found:
                return -1

        return swap

# @lc code=end
