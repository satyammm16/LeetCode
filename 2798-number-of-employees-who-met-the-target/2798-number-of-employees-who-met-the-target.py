class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        t=0
        for i in range(len(hours)):
            if hours[i]>=target:
                t+=1
        return t
        