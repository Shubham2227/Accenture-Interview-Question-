Alice and String
Alice has a peculiar fondness for strings without any interruptions. She considers "." as an interruption. You are given a string S and your task is to find and return
the length of the longest uninterrupted substring to match alices' fondness.
128020
Input Specification:
01032
input1: A string value S.
Output Specification:
Return an integer value representing the length of the longest uninterrupted substring to match alices' fondness.
S = "this.is.a.debugwithshubham"
output: 16 
For the input string "this.is.a.debugwithshubham", the uninterrupted substrings are "this" and "is" and "a" and "debugwithshubham". The longest substring is "debugwithshubham", 
and its length is 6


  *******************************   Solution 1 Using Split *************************

  
  public class LongestUninterruptedSubstring {
    public static int longestUninterruptedSubstring(String S) {
        
        String[] substrings = S.split("\\.");  
        int maxLength = 0;
        for (String substring : substrings) {
            if (substring.length() > maxLength) {
                maxLength = substring.length();
            }
        }
        return maxLength;
    }
    public static void main(String[] args) {
        String S = "this.is.a.debugwithshubham";
        int output = longestUninterruptedSubstring(S);
        System.out.println(output);  
    }
}

*******************************   Solution 1 without  Split *************************

public class LongestUninterruptedSubstring {
    public static int longestUninterruptedSubstring(String S) {
        int maxLength = 0;
        int currentLength = 0;
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == '.') {
                maxLength = Math.max(maxLength, currentLength);
                currentLength = 0;
            } else {
                currentLength++;
            }
        }
        maxLength = Math.max(maxLength, currentLength);

        return maxLength;
    }
    public static void main(String[] args) {
        String S = "this.is.a.debugwithshubham";
        int output = longestUninterruptedSubstring(S);
        System.out.println(output);  
    }
}
