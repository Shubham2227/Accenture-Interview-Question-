White Space Difference
You are given 2 strings A and B. Your task is to find and return a string saying 'Even' so if the value representing the absolute differences between the number of
whitespaces in both the strings is divisible by 2 else 'Odd' if the value representing the absolute differences between the number of whitespaces in both the strings 
the whitespace is not divisible by 2 along with the difference value
Input Specification: input1 : A string A input2: A string B
Output Specification:
Return a string saying 'Even' if the value representing the absolute differences between the number of whitespaces in both the strings is divisible by 2 else
'Odd' if the value representing the absolute differences between the number of whitespaces in both the strings the whitespace is not divisible by 2

Example 1:
inputl: "He ll o W or Id" input2 : "Hello World"
Output : Even4

********************* Solution - 1 Brute Force ******************



s1 ="He ll o W or id"
s2 = "Hello World"
count_s1= 0
count_s2 = 0
for i in s1:
    if i == " ":
        count_s1 += 1
for j in s2:
    if j  == " ":
        count_s2 += 1
diff = abs(count_s1 - count_s2)
if diff %2 == 0:
    print(f"Even{diff}")
else:
    print(f"Odd{diff}")

********************* Solution - 2 using Count ******************

def whitespace_difference(A, B):
    # Count whitespaces in both strings
    count_A = A.count(' ')
    count_B = B.count(' ')
    
    # Calculate absolute difference
    difference = abs(count_A - count_B)
    
    # Check divisibility by 2
    if difference % 2 == 0:
        return f"Even{difference}"
    else:
        return f"Odd{difference}"

# Example usage:
A = "He ll o W or Id"
B = "Hello World"
print(whitespace_difference(A, B))  # Output: "Even4"

********************* Solution - 3 using RE ******************

import re

def whitespace_difference_regex(A, B):
    # Use regex to count whitespaces
    count_A = len(re.findall(r'\s', A))
    count_B = len(re.findall(r'\s', B))
    
    # Calculate absolute difference
    difference = abs(count_A - count_B)
    
    # Check divisibility by 2
    if difference % 2 == 0:
        return f"Even{difference}"
    else:
        return f"Odd{difference}"

# Example usage:
A = "He ll o W or Id"
B = "Hello World"
print(whitespace_difference_regex(A, B))  # Output: "Even4"


********************* Solution - 4 using Collections ******************

from collections import Counter

def whitespace_difference_counter(A, B):
    # Count occurrences of all characters
    counter_A = Counter(A)
    counter_B = Counter(B)
    
    # Extract the whitespace counts
    count_A = counter_A.get(' ', 0)
    count_B = counter_B.get(' ', 0)
    
    # Calculate absolute difference
    difference = abs(count_A - count_B)
    
    # Check divisibility by 2
    if difference % 2 == 0:
        return f"Even{difference}"
    else:
        return f"Odd{difference}"

# Example usage:
A = "He ll o W or Id"
B = "Hello World"
print(whitespace_difference_counter(A, B))  # Output: "Even4"


