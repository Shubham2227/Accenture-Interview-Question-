Problem Statement:
You are given a string, the length of the string, and a character. Your task is to determine how many times the given character occurs in the string.
Write a function that returns an integer representing the number of times the specified character appears in the string.
Input:
input1: A string s of length n (1 ≤ n ≤ 10^5).
input2: An integer n, representing the length of the string s.
input3: A single character c that needs to be counted in the string.
Output:
Return an integer representing the number of occurrences of the character c in the string s.
Constraints:
The length of the string n is between 1 and 100,000.
The string will only contain lowercase English letters.
The character c is guaranteed to be a lowercase English letter.
The value of n will always match the actual length of the string. If not, return an appropriate error message.

Input:
input1: "helloworld"       .
input2: 10
input3: "l"

Output:
3

Explanation:
The string is "helloworld" .with a length of 10, and the character 'l' occurs 3 times in the string 


************************ Solution-1 **********************

def count_occurrences(string, length, char_to_find):
    if len(string) != length:
        return "Input length does not match the actual string length"
    count = string.count(char_to_find)
    return count

# Example 1
input1 = "helloworld"
input2 = 10
input3 = "l"
output = count_occurrences(input1, input2, input3)
print(f"Output: {output}")


************************ Solution-2 **********************


def count_occurrences(string, length, char_to_find):
    if len(string) != length:
        return "Input length does not match the actual string length"
    count = 0
    for char in string:
        if char == char_to_find:
            count += 1
    return count
input1 = "helloworld"
input2 = 10
input3 = "l"
output = count_occurrences(input1, input2, input3)
print(f"Output: {output}")
