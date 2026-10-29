class Solution(object):
    def largestAltitude(self, gain):
        x=0
        y=0
        for i in range(len(gain)):
            x+=gain[i]
            if x>y:
                y=x
        return y            
                   
        