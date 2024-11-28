# https://leetcode.com/problems/two-sum/


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            value = target - nums[i]
            if value in nums and nums[i] != value:
                return [i, nums.index(value)]
            if value in nums and nums.count(value) > 1:
                return [i, nums.index(value, i+1)]          
        return




print(Solution.twoSum(Solution(),[2,7,11,15], 9))