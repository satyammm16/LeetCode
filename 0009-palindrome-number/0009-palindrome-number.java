class Solution {
    public boolean isPalindrome(int x) {
        int original = x;
        int p=0;
        while(x>0){
            int a=x%10;
            p=p*10+a;
            x=x/10;
        }
        if(p==original){
            return true;
        }
        else{
            return false;
    }
        
    }
}