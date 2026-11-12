class Solution(object):
    def countSeniors(self, details):
        count=0
        for i in range(len(details)):
            x=int(details[i][11:13])
            if x>60:
                count+=1
        return count