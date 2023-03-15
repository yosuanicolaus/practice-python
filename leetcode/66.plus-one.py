#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] == 10:
                digits[i] = 0
            else:
                break

        if digits[0] == 0:
            # append 1 to start of list
            temp = 1
            for i in range(len(digits)):
                digits[i], temp = temp, digits[i]
            digits.append(temp)

        return digits


# @lc code=end
