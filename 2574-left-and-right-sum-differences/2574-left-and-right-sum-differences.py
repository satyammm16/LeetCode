class Solution(object):
    def leftRightDifference(self, nums):
        l=0
        r=0
        z=[]
        for i in range(len(nums)):
            r+=nums[i]
        for i in range(len(nums)):
            r-=nums[i]
            z.append(abs(l-r))
            l+=nums[i]

        return z