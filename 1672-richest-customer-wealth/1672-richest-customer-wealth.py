class Solution(object):
    def maximumWealth(self, accounts):
        
        x=0
        sum=0
        for i in accounts:
            x=0
            for j in range(len(i)):
                x+=i[j]
            if sum<x:
                sum=x

        return sum
                
        