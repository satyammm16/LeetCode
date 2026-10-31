class Solution(object):
    def sortSentence(self, s):
        b = s.split(" ")
        x = [""] * len(b)
        for i in range(len(b)):
            pos = int(b[i][-1])
            word = b[i][:-1]
            x[pos - 1] = word
        z = ""
        for i in range(len(x)):
            z = z + x[i]
            if i != len(x) - 1:
                z = z + " "
        return z