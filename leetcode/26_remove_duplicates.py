class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        state = -101
        length = 0
        updater = 0

        for num in nums:
            if num != state:
                state = num
                nums[updater] = num
                length += 1
                updater += 1

        return length


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
