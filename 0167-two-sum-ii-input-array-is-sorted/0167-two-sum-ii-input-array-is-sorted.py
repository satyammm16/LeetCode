class Solution(object):
    def twoSum(self, numbers, target):
        z={}
        for i in range(len(numbers)):
            r=target-numbers[i]
            if r in z:
                return(z[r]+1,i+1)
            else:
                z[numbers[i]]=i
            

                    

        