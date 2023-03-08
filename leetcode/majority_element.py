class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nh = {}
        majority = nums[0]
        biggest_count = 1
        for num in nums:
            nh.setdefault(num, 0)
            nh[num] += 1
            if nh[num] > biggest_count:
                biggest_count = nh[num]
                majority = num

        return majority


s = Solution()
print(s.majorityElement([3, 2, 3]))
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
