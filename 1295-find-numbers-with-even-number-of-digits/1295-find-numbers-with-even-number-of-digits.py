class Solution(object):
    def findNumbers(self, nums):
        total=0
        for i in range(0,len(nums)):
            count=0
            while nums[i]>0:
                digit=nums[i]%10
                count=count+1
                nums[i]=nums[i]//10
            if count%2==0:
                total+=1
        return total

        