class Solution(object):
    def checkIfPangram(self, sentence):
        letters = []

        for i in sentence:
            if i not in letters:
                letters.append(i)

        if len(letters) == 26:
            return True
        else:
            return False