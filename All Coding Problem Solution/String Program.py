String Program
Problem: Alice is working on a system that processes text inputs from users. One of the requirements is that the text must not contain the substring "ppp" — three consecutive 'p' characters. If this substring appears, the text is rejected. To make the input text acceptable, Alice needs to remove characters in such a way that the substring "ppp" does not exist.

Your task is to help Alice by determining the minimum number of characters that need to be removed from the text to ensure no substring "ppp" is present.

Notes:
The string only contains lowercase alphabetic characters.
You can delete characters from any position in the string (not necessarily consecutive).
Ensure the result is non-negative.
Input Specification:
Input1: A string S, representing the text inputs from users.
Output Specification:
Return an integer value representing the minimum number of characters that need to be removed from the string S to avoid the substring "ppp".


Example 1:
Input:
S = "pppppp"
Output:
4
Explanation: The string contains 6 'p' characters. To make the string acceptable, at least 4 'p' characters must be removed to prevent three consecutive 'p's. After removing 4 characters, we would be left with "pp" or "p", both of which are valid.

Example 2:
Input:
S = "apbpppqp"
Output:
1



def min_removals_to_avoid_ppp(S):
    n = len(S)
    removals = 0
    i = 0
    
    # Iterate through the string
    while i < n:
        # Check for a 'ppp' sequence
        if i + 2 < n and S[i] == 'p' and S[i+1] == 'p' and S[i+2] == 'p':
            removals += 1  # Increment removal counter
            i += 3  # Skip ahead by 3 to move past the "ppp" sequence
        else:
            i += 1  # Move to the next character if no "ppp" found
    
    return removals

# Example test cases
print(min_removals_to_avoid_ppp("pppppp"))     # Output: 4
print(min_removals_to_avoid_ppp("apbpppqp"))   # Output: 1
print(min_removals_to_avoid_ppp("abcde"))      # Output: 0


