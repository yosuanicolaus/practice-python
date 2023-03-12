from math import sqrt, ceil
#
# @lc app=leetcode id=1952 lang=python3
#
# [1952] Three Divisors
#

# @lc code=start


class Solution:
    def isThree(self, n: int) -> bool:
        # every integer have at least 2 divisor: 1, and the number
        # 3 divisor means between 1 and the number there
        # must be exactly 1 integer divisor
        count = 0

        for num in range(2, n//2 + 1):
            if n % num == 0:
                count += 1
                if count > 1:
                    return False

        return count == 1


# @lc code=end

Solution().isThree(14)
