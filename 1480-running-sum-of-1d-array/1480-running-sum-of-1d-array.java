class Solution {
    public int[] runningSum(int[] nums) {
        int[] arr=new int[nums.length];
        int total=0;
        for (int i=0;i<nums.length;i++){
            total=total+nums[i];
            arr[i]=total;
        }
        return arr;
        
    }
}