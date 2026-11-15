class Solution(object):
    def alternateDigitSum(self, n):
        ans=0
        count=0
        rev=0
        while n>0:
            b=n%10
            rev=rev*10+b
            n=n//10
        while rev>0:
            a=rev%10
            count+=1
            rev=rev//10
            if count%2!=0:
                ans+=a
            else:

                ans-=a
        return ans
            
        