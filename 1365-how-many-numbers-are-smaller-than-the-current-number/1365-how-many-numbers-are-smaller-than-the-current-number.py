class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        o=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            o.append(count)
        return o
        

        