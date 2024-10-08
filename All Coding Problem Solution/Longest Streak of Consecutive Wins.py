Longest Streak of Consecutive Wins
Maximum Consecutive Ones


You are developing a feature for a mobile game that tracks player performance. The agame records the results of consecutive rounds as a binary array A, 
where 1 indicates a win and 0 indicates a loss. The game developers want to analyze how well players are doing by determining the longest 
streak of consecutive wins. Your task is to find and a300 retur an integer value representing the count of the maximum number of consecutive
1s (wins) in the array.
Input Specification:
input1: A binary integer array A representing the game records. input2: An integer value representing the number of games played.
Output Specification:
Return an integer value representing the count of the maximum number of consecutive 1s (wins) in the array.
Example 1:
input1: (1,1,0,1,1,1)
input2 : 6


********************** Solution 1. Brute Force Solution (O(n^2)) *********************************

def max_consecutive_ones_bruteforce(A, n):
    max_count = 0
    for i in range(n):
        if A[i] == 1:
            current_count = 0
            for j in range(i, n):
                if A[j] == 1:
                    current_count += 1
                    max_count = max(max_count, current_count)
                else:
                    break
    return max_count

# Example
A = [1, 1, 0, 1, 1, 1]
n = 6
print(max_consecutive_ones_bruteforce(A, n))  # Output: 3


********************** Solution  2. Linear Scan (O(n)) ********************** 

def max_consecutive_ones_linear(A, n):
    max_count = 0
    current_count = 0
    
    for i in range(n):
        if A[i] == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
            
    return max_count

# Example
A = [1, 1, 0, 1, 1, 1]
n = 6
print(max_consecutive_ones_linear(A, n))  # Output: 3

********************** Solution  3. Optimized Sliding Window (O(n)) ********************** Solution 

def max_consecutive_ones_sliding_window(A, n):
    max_count = 0
    current_count = 0
    for i in range(n):
        if A[i] == 1:
            current_count += 1
        else:
            current_count = 0
        max_count = max(max_count, current_count)
    return max_count

# Example
A = [1, 1, 0, 1, 1, 1,0,1,1,0,1,1,1,1]
n = 14
print(max_consecutive_ones_sliding_window(A, n)) 



