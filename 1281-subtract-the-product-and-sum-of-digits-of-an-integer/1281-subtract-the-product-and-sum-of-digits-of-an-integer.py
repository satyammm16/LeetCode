class Solution(object):
    def subtractProductAndSum(self, n):
        sum=0
        pro=1
        while n>0:
            x=n%10
            sum+=x
            pro=pro*x
            n=n//10
        return pro-sum

        