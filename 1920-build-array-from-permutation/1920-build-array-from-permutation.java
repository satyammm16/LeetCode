class Solution {
    public int[] buildArray(int[] nums) {
        int[] arr=nums;
        int[] f=new int[nums.length];
        for (int i=0;i<nums.length;i++)
        {
            int x=arr[nums[i]];
            f[i]=x;
        }
        return f;
        
    }
}