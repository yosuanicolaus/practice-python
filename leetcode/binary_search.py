# binary search (easy) - https://leetcode.com/problems/binary-search/
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # use two-pointer in a while loop instead of recursive
        l, r = 0, len(nums) - 1

        if l == r:
            if nums[0] == target:
                return 0
            return -1

        while l < r:
            mid = (l + r) // 2
            val = nums[mid]

            print("mid", mid)

            if r - l == 1 and nums[l] != target and nums[r] != target:
                break

            if target < val:
                r = mid
            elif target > val:
                l = mid
            else:
                return mid

        return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))

print(s.search([-1, 0, 3, 5, 9, 12], 2))

print(s.search([0, 1, 2, 3, 4, 6, 7, 8, 9], 5))
