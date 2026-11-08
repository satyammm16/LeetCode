class Solution(object):
    def repeatedCharacter(self, s):
        q=[]
        for i in range(len(s)):
            if s[i] in q:
                return s[i]
            else:
                q.append(s[i])

        
        