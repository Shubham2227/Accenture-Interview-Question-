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

def longest_uninterrupted_substring(S):
    substrings = S.split('.')
    max_length = 0
    for substring in substrings:
        if len(substring) > max_length:
            max_length = len(substring)
    return max_length
    
S = "this.is.a.debugwithshubham"
output = longest_uninterrupted_substring(S)
print(output) 

*******************************   Solution 1 without  Split *************************

def longest_uninterrupted_substring(S):
    max_length = 0
    current_length = 0
    for char in S:
        if char == '.':
            max_length = max(max_length, current_length)
            current_length = 0
        else:
            current_length += 1
    max_length = max(max_length, current_length)
    return max_length
S = "this.is.a.debugwithshubham"
output = longest_uninterrupted_substring(S)
print(output) 



