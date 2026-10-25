class Solution(object):
    def differenceOfSums(self, n, m):
        div=0
        not_div=0
        for i in range(0,n+1):
            if i%m==0:
                div+=i
            else:
                not_div+=i
        return not_div-div

