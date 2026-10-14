class Solution(object):
    def maximumWealth(self, accounts):
        sum=[]
        l=0
        for i in accounts:
            x=0
            for j in range(len(i)):
                x=x+i[j]
            sum.append(x)
        for k in range(len(sum)):
            if sum[k] >l:
                l=sum[k]
        return l
                
        