#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        fleet = 0
        highest = float('-inf')

        for p, s in sorted(pair)[::-1]:
            time = (target - p) / s
            if time > highest:
                highest = time
                fleet += 1

        return fleet


# @lc code=end
target = 20
position = [6, 2, 17]
speed = [3, 9, 2]
s = Solution()
print(s.carFleet(target, position, speed))
