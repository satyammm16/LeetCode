class Solution(object):
    def mostWordsFound(self, sentences):
        max=0
        for i in range(len(sentences)):
            x=1
            for j in range(len(sentences[i])):
                if sentences[i][j]==' ':
                    x+=1
            if x>max:
                max=x
        return max 
        