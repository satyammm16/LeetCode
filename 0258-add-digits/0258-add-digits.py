class Solution:
    def addDigits(self, num: int) -> int:
        while 9<num:
            total=0
            while num>0:
                digit=num%10
                total=total+digit
                num=num//10
            num=total
        return num

            

        

        return total
        