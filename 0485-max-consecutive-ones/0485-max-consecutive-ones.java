class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count=0;
        int max=0;
        for(int i=0;i<nums.length;i++){
            
            if(nums[i]==1){
                max++;
            }
            else{
            max=0;
        }
        if(count<max){
            count=max;
        }
        }
        return count;
        
    }
}