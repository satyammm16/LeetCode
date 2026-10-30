class Solution(object):
    def truncateSentence(self, s, k):
        b=s.split(" ")
        x=""
        for i in range(k):
            x=x+b[i]
            if i!=k-1:
                x=x+" "
        return x
        
        