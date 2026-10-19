class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        total=0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i]==stones[j]:
                    total+=1
        return total