class Solution(object):
    def numberOfSteps(self, num):
        sum=0
        x=num
        while x>0:
            if x%2==0:
                x=x//2
            else:
                x=x-1
            sum+=1
        return sum
                
        



        