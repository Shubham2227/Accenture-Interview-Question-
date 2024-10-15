
// Alice and String
// Alice has a peculiar fondness for strings without any interruptions. She considers "." as an interruption. You are given a string S and your task is to find and return the length of the longest uninterrupted substring to match alices' fondness.
// 128020
// Input Specification:
// 01032
// input1: A string value S.
// Output Specification:
// Return an integer value representing the length of the longest uninterrupted substring to match alices' fondness.
// S = "this.is.a.debugwithshubham"
// output: 16 
// For the input string "this.is.a.debugwithshubham", the uninterrupted substrings are "this" and "is" and "a" and "debugwithshubham". The longest substring is "debugwithshubham", and its length is 6

import java.util.*;

public class AliceandString {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        sc.close();
        System.out.println(findLongestWord(s));
    }

    public static String findLongestWord(String str) {
        int max = 0;
        int count = 0;
        String str1 = "";

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '.') {
                max = Math.max(max, count);
                count = 0;
            }

            else
                count++;

        }
        max = Math.max(max, count);

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '.') {
                if (str1.length() == max) {
                    return str1;
                } else
                    str1 = "";
            }

            else
                str1 = str1 + str.charAt(i);

        }
        return null;
    

    }

}
