class Solution {
    public int[] getConcatenation(int[] nums) {
        int c =nums.length;
        int[] arr=new int[2*c];
        for (int i=0;i<nums.length;i++){
            arr[i]=nums[i];
            arr[i+c]=nums[i];

            
        } 
        return arr;

        
    }
}