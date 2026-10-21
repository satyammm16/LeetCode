class Solution(object):
    def twoSum(self, nums, target):
        z={}
        for i in range(0,len(nums)):
            r=target-nums[i]
            if r in z:
                return(z[r],i)
            else:
                z[nums[i]]=i
        