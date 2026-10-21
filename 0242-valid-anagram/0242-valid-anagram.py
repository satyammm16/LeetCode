class Solution(object):
    def isAnagram(self, s, t):

        if len(s)==len(t):
            freq={}
            for i in range(len(s)):
                if s[i] in freq:
                    freq[s[i]]=freq[s[i]]+1
                else:
                    freq[s[i]]=1
                
            freq1={}
            for j in range(len(t)):
                if t[j] in freq1:
                    freq1[t[j]]=freq1[t[j]]+1
                else:
                    freq1[t[j]]=1
            if freq==freq1:
                return True
            else:
                return False
                
        else:
            return False

        