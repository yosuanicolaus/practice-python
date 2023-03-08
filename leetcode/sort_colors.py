class Solution:
    def sortColors(self, nums: list[int]) -> None:
        c0, c1, c2 = 0, 0, 0
        for n in nums:
            if n == 0:
                c0 += 1
            elif n == 1:
                c1 += 1
            else:
                c2 += 1

        for i in range(len(nums)):
            if c0 > 0:
                c0 -= 1
                nums[i] = 0
            elif c1 > 0:
                c1 -= 1
                nums[i] = 1
            else:
                c2 -= 1
                nums[i] = 2
