class Solution(object):
    def numOfStrings(self, patterns, word):
    
        z=0
        for i in range(len(patterns)):
            if patterns[i] in word:
                z+=1
                
        return z
        