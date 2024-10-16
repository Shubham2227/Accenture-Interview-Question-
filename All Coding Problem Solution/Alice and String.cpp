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

  
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;
vector<string> split(const string &S, char delimiter) {
    vector<string> substrings;
    stringstream ss(S);
    string temp;
    while (getline(ss, temp, delimiter)) {
        substrings.push_back(temp);
    }
    return substrings;
}
int longestUninterruptedSubstring(const string &S) {
    vector<string> substrings = split(S, '.');  
    int maxLength = 0;
    for (const string &substring : substrings) {
        if (substring.length() > maxLength) {
            maxLength = substring.length();
        }
    }
    return maxLength;
}
int main() {
    string S = "this.is.a.debugwithshubham";
    int output = longestUninterruptedSubstring(S);
    cout << output << endl;  
    return 0;
}



*******************************   Solution 1 without  Split *************************



  #include <iostream>
#include <string>
using namespace std;
int longestUninterruptedSubstring(const string &S) {
    int maxLength = 0;
    int currentLength = 0;
    for (char c : S) {
        if (c == '.') {
            maxLength = max(maxLength, currentLength);
            currentLength = 0;
        } else {
            currentLength++;
        }
    }
    maxLength = max(maxLength, currentLength);
    return maxLength;
}
int main() {
    string S = "this.is.a.debugwithshubham";
    int output = longestUninterruptedSubstring(S);
    cout << output << endl;  
    return 0;
}
