class Solution(object):
    def findLengthOfLCIS(self, nums):
        count=1
        z=1
        for i in range(len(nums)-1):              
            if nums[i]<nums[i+1] :
                z+=1
            else:
                z=1
            if count<z:
                count=z           
        
            
        return count




        