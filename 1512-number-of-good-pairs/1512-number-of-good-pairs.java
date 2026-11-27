class Solution {
    public int numIdenticalPairs(int[] nums) {
        ArrayList<Integer> list=new ArrayList<>();
        for (int i=0;i<nums.length-1;i++){
            int count=0;
            for (int j=i+1;j<nums.length;j++){
                if(nums[i]==nums[j]){
                    count+=1;
                }
                

            }
            list.add(count);
        
        }
        int ans=0;
        for(int i=0;i<list.size();i++){
            ans+=list.get(i);

        }
        return ans;
    }
}