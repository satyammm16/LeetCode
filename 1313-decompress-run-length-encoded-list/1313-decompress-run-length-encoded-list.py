class Solution(object):
    def decompressRLElist(self, nums):
        lst=[]
        for i in range(0,len(nums),2):
            freq=nums[i]
            value=nums[i+1]
            for j in range(freq):
                lst.append(value)
        return lst                
        