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
returned as the output

  

#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

string maxVowelOccurrence(const string& P) {
    string vowels = "AEIOU";
    unordered_map<char, int> count;
    for (char v : vowels) {
        count[v] = 0; 
    for (char ch : P) {
        if (count.find(ch) != count.end()) {
            count[ch]++;
        }
    }
    char maxVowel = '\0';
    int maxCount = 0;

    for (char v : vowels) {
        if (count[v] > maxCount) {
            maxVowel = v;
            maxCount = count[v];
        }
    }
    if (maxVowel != '\0') {
        return string(1, maxVowel) + ":" + to_string(maxCount);
    } else {
        return "No vowels found";
    }
}
int main() {
    string P = "THIS IS NOT AN INTEGER VALUE";
    cout << maxVowelOccurrence(P) << endl;  // Output: E:3
    return 0;
}
