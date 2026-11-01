class Solution(object):
    def isSameAfterReversals(self, num):
        r=0
        o=num
        while num>0:
            x=num%10
            r=r*10+x
            num=num//10
        num=r
        r=0
        while num>0:
            y=num%10
            r=r*10+y
            num=num//10
        return o==r
        