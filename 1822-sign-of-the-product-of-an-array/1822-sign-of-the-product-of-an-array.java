class Solution {
    public int arraySign(int[] nums) {
        int signCnt = 0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] < 0) signCnt++;
            else if(nums[i] == 0) return 0;
        }
        if(signCnt % 2 == 0) return 1;
        else return -1;
    } 
}