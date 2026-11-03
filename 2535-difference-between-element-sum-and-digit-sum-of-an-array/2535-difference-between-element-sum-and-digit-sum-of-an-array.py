class Solution(object):
    def differenceOfSum(self, nums):
        st=0
        t=0
        for i in range(len(nums)):
            st+=nums[i]
            num=nums[i]
            while num>0:
                a=num%10
                t+=a
                num=num//10
        return st-t
        