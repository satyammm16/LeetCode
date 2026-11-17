class Solution(object):
    def sumBase(self, n, k):
        
        ans=0
        while n>0:
            a=n%k
            ans+=a
            n=n//k
        return ans


        