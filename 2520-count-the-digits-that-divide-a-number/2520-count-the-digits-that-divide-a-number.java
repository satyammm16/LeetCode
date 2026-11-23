class Solution {
    public int countDigits(int num) {
        int output=0;
        int x=num;
        while(num>0){
            int a=num%10;
            num=num/10;
            if(x%a==0){
                output+=1;
            }
        }
        return output;
        
    }
}