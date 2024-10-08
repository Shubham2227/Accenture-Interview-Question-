Maximum Vowel Frequency in a Paragraph
Most Frequent Vowel

  
Mike has written an English paragraph P on the white board, all in upper case. The paragraph contains vowels and consonants. His goal is to find that vowel which has occurred maximum times. He is writing the vowels as "E:19" which means E has occurred maximum times in paragraph P and the count is 19, separated with a :. Your task is to find and return a string representing that vowel and its respective occurrence If no vowel is found, then return "No vowels found". If there is a conflict between two vowels with same occurrence, then return the vowel that arrives first in lexicographic order.
Input Specification:
input1: A string value P representing the paragraph written on the white board
Output Specification:
Return a string representing the vowel with the maximum occurrence along with its respective occurrence. If no vowel is found, then return "No vowels found". If there is a conflict between two vowels with same occurrence, then return the vowel that arrives first in lexicographic order.
xample 1:
input1: THIS IS NOT AN INTEGER VALUE Output: E3
Explanation:
Here, paragraph P is "THIS IS NOT AN INTEGER VALUE",
", Below are the counts of ea
vowel:
• A:2
• E:3
• I:3
• 0:1
• U:1
We can see that the alphabet E and I occurred 3 times, which is maximum. Since E comes before lin lexicographic order, 'E' will be given the preference. Therefore, E:
returned as the output.

import java.util.HashMap;
import java.util.Map;

public class MaxVowelOccurrence {
    public static String maxVowelOccurrence(String P) {
        String vowels = "AEIOU";
        Map<Character, Integer> count = new HashMap<>();
        for (char v : vowels.toCharArray()) {
            count.put(v, 0); 
        for (char ch : P.toCharArray()) {
            if (count.containsKey(ch)) {
                count.put(ch, count.get(ch) + 1);
            }
        }
        char maxVowel = 0;
        int maxCount = 0;
        for (char v : vowels.toCharArray()) {
            if (count.get(v) > maxCount) {
                maxVowel = v;
                maxCount = count.get(v);
            }
        }
        if (maxVowel != 0) {
            return maxVowel + ":" + maxCount;
        } else {
            return "No vowels found";
        }
    }
    public static void main(String[] args) {
        String P = "THIS IS NOT AN INTEGER VALUE";
        System.out.println(maxVowelOccurrence(P));  // Output: E:3
    }
}
