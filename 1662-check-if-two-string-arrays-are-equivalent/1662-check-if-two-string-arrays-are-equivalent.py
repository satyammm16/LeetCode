class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s=""
        s1=""
        for i in range(len(word1)):
            s+=word1[i]
        for j in range(len(word2)):
            s1+=word2[j]
        if s==s1:
            return True
        else:
            return False