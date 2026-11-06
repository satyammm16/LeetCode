class Solution(object):
    def maximumCount(self, nums):
        p=0
        n=0
        for i in range(len(nums)):
            if nums[i]>0:
                p+=1
            elif nums[i]<0:
                n+=1
        if p>n:
            return p
        else:
            return n
        