class Solution(object):
    def minOperations(self, nums):
        count=0
        for i in range(len(nums)-1):
           
            if nums[i+1]<=nums[i]:
                diff=nums[i]+1-nums[i+1]
                count+=diff
                nums[i+1]=nums[i]+1
        return count
        