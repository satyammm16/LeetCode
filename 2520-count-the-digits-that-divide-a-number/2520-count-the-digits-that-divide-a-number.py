class Solution(object):
    def countDigits(self, num):
        z=num
        y=0
        while num>0:
            x=num%10
            if z%x==0:
                y+=1
            
            num=num//10
        return y


        