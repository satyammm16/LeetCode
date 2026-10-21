class Solution(object):
    def moveZeroes(self, nums):
        lst=[]
        z=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                lst.append(nums[i])
        n=len(nums)-len(lst)
        for i in range(n):
            lst.append(0)
        for i in range(len(lst)):
            nums[i] = lst[i]
        return nums
        

