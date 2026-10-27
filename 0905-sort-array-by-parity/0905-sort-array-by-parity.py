class Solution(object):
    def sortArrayByParity(self, nums):
        z=[]
        if len(nums)==0:
            return [0]
        else:
            for i in range(len(nums)):
                if nums[i]%2==0:
                    z.append(nums[i])
            for i in range(len(nums)):
                if nums[i]%2!=0:
                    z.append(nums[i])
            return z
