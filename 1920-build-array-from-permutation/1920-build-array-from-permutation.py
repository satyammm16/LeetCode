class Solution(object):
    def buildArray(self, nums):
        lst=nums
        f=[]
        for i in range(len(nums)):
            x=lst[nums[i]]
            f.append(x)
        return f
        