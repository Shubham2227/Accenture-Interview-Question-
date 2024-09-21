The Clock Problem
Your friend has problem in reading the time if a clock follows 24-hour format so you decide to help him out. You have two integers X and Y. 
Your task is to find and return an integer value representing the product of these two integers in the 12-hour system.
Input Specification:
inputt: An integer value X input2: An integer value Y
Output Specification:
Return an integer value representing the product of the two integers in the 12-
hour system.
Example: 
inputt:4
input2: 5
Output: 8

def clock_problem(inputt, input2):
    # Calculate the product of the two integers
    product = inputt * input2
    
    # Find the result modulo 12
    result = product % 12
    
    # If result is 0, return 12 (since 0 on a clock is equivalent to 12)
    if result == 0:
        return 12
    else:
        return result

# Test case 1
print(clock_problem(4, 5))  # Output: 8

# Test case 2
print(clock_problem(6, 2))  # Output: 12
