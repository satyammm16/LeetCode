class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        total=0
        for i in range(len(startTime)):
                if  startTime[i]<=queryTime and endTime[i]>=queryTime:
                    total+=1
        return total

        