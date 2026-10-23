class Solution(object):
    def findWordsContaining(self, words, x):
        z=[]
        for i in range(len(words)):
            if x in words[i]:
                z.append(i)
        return z